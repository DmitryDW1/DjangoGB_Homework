from random import randint, choice
from django.core.management.base import BaseCommand, CommandParser
from shop_app.models import Client, Order, Product, ProductsInOrder
from datetime import datetime, timedelta

MAX_PRODUCTS = 100
MAX_PRODUCTS_IN_ORDER = 10
MIN_PRICE = 50
MAX_PRICE = 999
START = datetime.strptime('07.04.2023', '%d.%m.%Y')
END = datetime.strptime('07.04.2024', '%d.%m.%Y')

class Command(BaseCommand):
    help = f'Заполнение таблиц тестовыми данными'
    
    def add_arguments(self, parser):
        parser.add_argument('clients', type=int, help=f'Генерация клиентов с заданным параметром "CLIENTS"')
        parser.add_argument('products', type=int, help=f'Генерация товаров с заданным параметром "PRODUCTS"')
        parser.add_argument('orders', type=int, help=f'Генерация заказов с заданным параметром "ORDERS"')
        
    def handle(self, *args, **options):
        count_clients = options['clients']
        count_products = options['products']
        count_orders = options['orders']
        clients = []
        products = []
        orders = []
        for i in range(1, count_clients + 1):
            client = Client(
                            name=f'Client_{i}', 
                            email=f'client{i}@testmail.com', 
                            phone_number=f'+7{randint(9000000000, 9999999999)}', 
                            addres=f'Client_addres_{i}',
                            date_reg=self.get_random_date(START, END)
                            )
            clients.append(client)
            client.save()
            
        for j in range(1, count_products + 1):
            product = Product(
                            name=f'Product_{j}',
                            description=f'Description_{j}',
                            price=randint(MIN_PRICE, MAX_PRICE),
                            quantity=randint(1, MAX_PRODUCTS),
                            date_of_addition=self.get_random_date(START, END)
                            )
            products.append(product)
            product.save()
            
        for client in clients:
            for _ in range(count_orders):
                order = Order.objects.create(customer=client)
                orders.append(order)
                
            for order in orders:
                products_in_order = randint(1, count_products)
                order.registration_date = self.get_random_date(START, END)
                for _ in range(products_in_order):
                    product = choice(products)
                    count_products_in_order = randint(1, MAX_PRODUCTS_IN_ORDER)
                    ProductsInOrder.objects.create(order=order, product=product, product_count=count_products_in_order)
                    order.total_cost += count_products_in_order * product.price
                    order.save()
            
        self.stdout.write('База данных успешно создана.')
        
    def get_random_date(self, start, end):
        delta = end - start
        return start + timedelta(randint(0, delta.days))
