from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = 'Update client'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Name client')
        parser.add_argument('email', type=str, help='Email client')
        parser.add_argument('phone_number', type=str, help='Phone number')
        parser.add_argument('addres', type=str, help='Addres')

    def handle(self, *args, **options):
        pk = options['pk']
        name = options['name']
        email = options['email']
        phone_number = options['phone_number']
        addres = options['addres']

        client = Client.objects.filter(pk=pk).first()

        if client:
            if name is not None:
                client.name = name
            if email is not None:
                client.email = email
            if phone_number is not None:
                client.phone_number = phone_number
            if addres is not None:
                client.addres = addres
            client.save()
            self.stdout.write(f'Client update succeful!')
        else:
            self.stdout.write(f'Client does not exist!')