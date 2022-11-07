from django.shortcuts import render

def review_bag(request):
    """ 
    A view that renders the shopping basket contents page
    """
    return render (request, 'bag/bag.html')