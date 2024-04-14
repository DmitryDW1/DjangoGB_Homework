from django.contrib import admin
from .models import Client, Product, Order, Category

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'addres', 'date_reg']
    search_fields = ['name', 'email', 'phone_number']
    ordering = ['-date_reg']
    list_filter = ['name']
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'date_of_addition', 'photo', ]
    search_fields = ['name', 'price', 'quantity']
    ordering = ['name']
    list_filter = ['name']

    fieldsets = [
        (
            'Общая информация',
            {
                'classes': ['wide'],
                'fields': ['name', 'description', 'photo', 'category'],
            },
        ),
        (
            'Бух учет',
            {
                'classes': ['collapse'],
                'fields': ['price', 'quantity'],
            }
        ),
    ]
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'registration_date']
    search_fields = ['customer']
    ordering = ['-customer']
    list_filter = ['registration_date']    
    readonly_fields =['registration_date']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Что купил',
            {
                'classes': ['wide'],
                'fields': ['products_in_order'],
            },
        ),
        (
            'Итоговая цена заказа',
            {
                'classes': ['wide'],
                'fields': ['total_cost'],
            },
        )
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
# Register your models here.
