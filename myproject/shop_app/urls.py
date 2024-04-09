from django.urls import path
from shop_app.views import index, about, list_clients, orders_client
from shop_app.views import products_period

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('list_clients/', list_clients, name='list_clients'),
    path('orders_client/<int:client_id>/', orders_client, name='orders_client'),
    path('products_period/<int:client_id>/', products_period, name='products_period'),
]