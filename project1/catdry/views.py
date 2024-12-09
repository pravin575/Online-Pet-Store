from django.shortcuts import render
from .models import Catdry
# Create your views here.

def home(request):
    context={}
    catdryy=Catdry.objects.all()
    print(catdryy)
    context['catdry']=catdryy
    return render(request,'catdry/catdry.html',context)


def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        catdryy=Catdry.objects.filter(id = pid)
        context['product']=catdryy
    return render(request,'catdry/product_details.html',context)