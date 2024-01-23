from django.contrib import admin
from .models import Product, Category, Category, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')

admin.site.register(Category)




# Register your models here.
