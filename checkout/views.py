from django.shortcuts import render

def review_checkout(request):
    """ 
    A view that renders the checkout contents page
    """
    return render(request, 'checkout/checkout.html')
