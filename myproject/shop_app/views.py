from datetime import datetime, timedelta
import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Client, Order, Product
from django.utils import timezone

logger = logging.getLogger(__name__)

def index(request):
    '''
    Главная страница сайта
    '''
    return render(request, 'shop_app/index.html')

def about(request):
    '''
    Страница с информацией об авторе сайта
    '''
    return render(request, 'shop_app/about.html')

def list_clients(request):
    clients = Client.objects.all()
    context = {
        'title': 'Список клиентов',
        'clients': clients
        }
    return render(request, 'shop_app/list_clients.html', context)

def orders_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client).all()
    context = {
        'title': client.id,
        'list': f'Имя: {client.name}',
        'orders': orders,
        'name': 'Список заказов клиента',
        'count': len(orders),
    }
    
    return render(request, 'shop_app/orders_client.html', context)

def products_period(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(customer=client, registration_date__gte=week_ago)
    orders_month = Order.objects.filter(customer=client, registration_date__gte=month_ago)
    orders_year = Order.objects.filter(customer=client, registration_date__gte=year_ago)

    products_week = set()
    products_month = set()
    products_year = set()

    for order in orders_week:
        products_week.update(order.products_in_order.all())

    for order in orders_month:
        products_month.update(order.products_in_order.all())

    for order in orders_year:
        products_year.update(order.products_in_order.all())

    context = {
        'title': 'Сортировка товаров по дате',
        'client': client,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }
    print(products_week)
    return render(request, 'shop_app/products_period.html', context)