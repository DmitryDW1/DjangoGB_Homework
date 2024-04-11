from datetime import datetime, timedelta
import logging
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Client, Order, Product
from django.utils import timezone
from .forms import ProductForm, AddProduct

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


def product_update(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            message = f"ТОвар с ID {product_id} успешно обновлён."
            return render(request, 'shop_app/product_update.html', {'form': form, 'message': message})
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'shop_app/product_update.html', {'form': form})


def create_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            photo = request.FILES.get('photo')
            if photo:
                new_product = Product(name=name, description=description, price=price, quantity=quantity, photo=photo)
            else:
                new_product = Product(name=name, description=description, price=price, quantity=quantity)
            new_product.save()
            message = f"Товар успешно создан с ID {new_product.pk}."
            return render(request, 'shop_app/create_product.html', {'form': form, 'message': message})
    form = AddProduct()
    return render(request, 'shop_app/create_product.html', {'form': form})


