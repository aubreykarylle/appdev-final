from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import ProductListView, create_product

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', create_product, name='create-product')
]

