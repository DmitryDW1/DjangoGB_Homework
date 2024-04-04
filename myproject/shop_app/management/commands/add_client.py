from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "Add new client"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name client')
        parser.add_argument('email', type=str, help='Email client')
        parser.add_argument('phone_number', type=str, help='Phone number')
        parser.add_argument('addres', type=str, help='Addres')

    def handle(self, *args, **options):
        name = options.get('name')
        email = options.get('email')
        phone_number = options.get('phone_number')
        addres = options.get('addres')

        client = Client(
            name=name, 
            email=email, 
            phone_number=phone_number, 
            addres=addres
            )
        client.save()
        self.stdout.write(f'{client}')