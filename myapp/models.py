from django.db import models
import datetime
from django.utils import timezone


# Categories of Products
class Category(models.Model):
        name = models.CharField(max_length=50)

        def __str__(self):
            return self.name
        
# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description =models.TextField(null=True, blank=True)
    image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


        
class Order (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quatity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField()
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product