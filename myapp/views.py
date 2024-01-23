from django.shortcuts import render, redirect

from django.views.generic import ListView, TemplateView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Change 'post_list' to your actual post list URL name
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})

# Create your views here.
