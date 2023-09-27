from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def calculate_total_price(self, quantity):
        return self.price * quantity

class Transaction_items(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)

class Transaction(models.Model):
    cashier = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_items = models.IntegerField()
    item = models.ManyToManyField(Product,through='Transaction_items')
    transaction_time = models.DateTimeField(auto_now=True)







