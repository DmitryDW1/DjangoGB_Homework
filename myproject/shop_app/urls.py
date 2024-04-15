from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from shop_app.views import create_product, index, about, list_clients, orders_client, product_update
from shop_app.views import products_period, list_products, get_product, get_order, total_in_db, total_in_template, total_in_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('list_clients/', list_clients, name='list_clients'),
    path('orders_client/<int:client_id>/', orders_client, name='orders_client'),
    path('products_period/<int:client_id>/', products_period, name='products_period'),
    path('product_update/<int:product_id>/', product_update, name='product_update'),
    path('create_product/', create_product, name='create_product'),
    path('list_products/', list_products, name='list_products'),
    path('get_product/<int:product_id>/', get_product, name='get_product'),
    path('get_order/<int:order_id>/', get_order, name='get_order'),
    # path('__debug__/', include ('debug_toolbar.urls')),
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)