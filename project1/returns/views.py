from django.shortcuts import render, redirect
from .models import Order, OrderReturn
from .forms import OrderReturnForm
from django.contrib import messages

# returns/views.py

from django.shortcuts import redirect

def return_order(request):
    if request.method == "POST":
        form = OrderReturnForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your return request has been submitted.")
            return redirect('return_success')
    else:
        form = OrderReturnForm(user=request.user)

    return render(request, 'returns/return_form.html', {'form': form})






from django.shortcuts import render

def return_success(request):
    return render(request, 'returns/return_success.html')