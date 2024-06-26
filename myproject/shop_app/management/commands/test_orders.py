from django.core.management.base import BaseCommand

from shop_app.models import Client, Order

from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = "Add new order"
    def handle(request, client_id):
        client = get_object_or_404(Client, pk=client_id)
        orders = Order.objects.filter(customer_id=client_id).all()
        context = {
            'title': client.id,
            'list': f'Имя: {client.name}',
            'items': orders,
            'name': 'order_products'
        }
        print (context)