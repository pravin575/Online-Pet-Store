from django.shortcuts import render
from .models import Kitten
# Create your views here.

def home(request):
    context={}
    kittenn=Kitten.objects.all()
    print(kittenn)
    context['kitten']=kittenn
    return render(request,'kitten/kitten.html',context)


def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        kittenn=Kitten.objects.filter(id = pid)
        context['product']=kittenn
    return render(request,'kitten/product_details.html',context)