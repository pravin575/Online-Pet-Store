from django.shortcuts import render, get_object_or_404
from .models import Order

def track_order(request):
    order_number = request.GET.get('order_number', None)
    order = None
    if order_number:
        order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'tracking/track_order.html', {'order': order})

