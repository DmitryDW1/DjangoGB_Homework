from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = 'Add new product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name product')
        parser.add_argument('description', type=str, help='Description product')
        parser.add_argument('price', type=float, help='Price')
        parser.add_argument('quantity', type=int, help='Quantity product')

    def handle(self, *args, **options):
        name = options.get('name')
        description = options.get('description')
        price = options.get('price')
        quantity = options.get('quantity')

        product = Product(
            name=name, 
            description=description, 
            price=price, 
            quantity=quantity
            )
        product.save()
        self.stdout.write(f'{product}')