from django.urls import path
from shop_app.views import create_product, index, about, list_clients, orders_client, product_update
from shop_app.views import products_period

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('list_clients/', list_clients, name='list_clients'),
    path('orders_client/<int:client_id>/', orders_client, name='orders_client'),
    path('products_period/<int:client_id>/', products_period, name='products_period'),
    path('product_update/<int:product_id>/', product_update, name='product_update'),
    path('create_product/', create_product, name='create_product'),
    
]