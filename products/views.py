from django.shortcuts import render
from .models import Product

def all_products(request):
    """ 
    A view to show all products
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render (request, 'products/products.html', context)

def product_detail(request, **kwargs):
    """ A view to show individual product details """
    pk = kwargs.get("pk")
    product = get_object_or_404(Product, id=pk)

    context = {
        'product': product,
    }

  