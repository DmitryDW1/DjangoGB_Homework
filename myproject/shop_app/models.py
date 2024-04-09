from datetime import datetime
from django.db import models


class Client(models.Model):
    name = models.TextField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, null=True)
    addres = models.TextField(max_length=200, null=True)
    date_reg = models.DateField()
    
    def __str__(self) -> str:
        return f'Name: {self.name}\
                \nE-mail: {self.email}\
                \nPhone number: {self.phone_number}\
                \nAddres: {self.addres}\
                \nDate registration: {self.date_reg}'
                
                
class Product(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)
    date_of_addition = models.DateField()
    
    def __str__(self) -> str:
        return f'ID: {self.id}\
                \nName: {self.name}\
                \nDescription: {self.description}\
                \nPrice: {self.price}\
                \nQuantity: {self.quantity}\
                \nDate of addition: {self.date_of_addition}'
                

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products_in_order = models.ManyToManyField(Product, related_name='products')
    total_cost = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    registration_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.pk}\
                \n{self.products_in_order}\
                \n{self.registration_date}'
    

    
# Create your models here.
