from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop_app.models import Product


class Command(BaseCommand):
    help = 'Update product'
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Description product')
        parser.add_argument('price', type=float, help='Product price')
        
    def handle(self, *args, **options):
        pk = options['pk']
        name = options['name']
        description = options['description']
        price = options['price']
        
        product = Product.objects.filter(pk=pk).first()
        
        if product:
            if name is not None:
                product.name = name
            if description is not None:
                product.description = description
            if price is not None:
                product.price = price
            product.save()
            self.stdout.write(f'Product update succeful!')
        else:
            self.stdout.write(f'Product does not exist!')