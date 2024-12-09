from django.shortcuts import render
from .models import Grain
# Create your views here.

def home(request):
    context={}
    dograinn=Grain.objects.all()
    print(dograinn)
    context['doggrain']=dograinn
    return render(request,'doggrain/doggrain.html',context)

def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        grainn=Grain.objects.filter(id = pid)
        context['product']=grainn
    return render(request,'doggrain/product_details.html',context)