from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = 'Delete product'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **options):
        pk = options.get('pk')

        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
            self.stdout.write(f'Product deleted!')
        else:
            self.stdout.write(f'Product does not exist!')