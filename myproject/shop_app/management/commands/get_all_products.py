from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = 'Get all clients'
    
    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            self.stdout.write(f'{product}\n----------')