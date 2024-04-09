from datetime import datetime, timedelta
import math
from random import randint, choice

from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order

MAX_PRODUCTS = 100
MAX_PRODUCTS_IN_ORDER = 10
MIN_PRICE = 50
MAX_PRICE = 999
START = datetime.strptime('07.04.2023', '%d.%m.%Y')
END = datetime.strptime('07.04.2024', '%d.%m.%Y')


class Command(BaseCommand):
    help = "Generate fake data for Customer, Product and Order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        qty_custs = count
        qty_prods = count ** 3
        qty_orders = count * 2

        clients = []
        products = []

        for i in range(1, qty_custs + 1):
            client = Client(
                name=f'name_{i}', 
                email=f'email{i}@testmail.com',
                phone_number=f'+79{randint(100_000_000, 999_999_999)}',
                addres=f'Addres_{i}',
                date_reg=self.get_random_date(START, END)
                )
            client.save()
            clients.append(client)

        for i in range(1, qty_prods + 1):
            product = Product(
                name=f'title_{i}', 
                description=f'description_{i}',
                price=randint(100, 100_000)/math.pi,
                quantity=randint(1, 200),
                date_of_addition=self.get_random_date(START, END)
                )

            product.save()
            products.append(product)

        for i in range(1, qty_orders + 1):
            order = Order(customer=choice(clients))
            order.save()
            sum = 0
            for _ in range(randint(1, qty_custs)):
                product = choice(products)
                sum += product.price
                order.products_in_order.add(product)
                # order.save()
            order.total_cost = sum
            order.save()
            
    def get_random_date(self, start, end):
        delta = end - start
        return start + timedelta(randint(0, delta.days))