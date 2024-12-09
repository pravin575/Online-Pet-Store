from django.shortcuts import render
from .models import Puppy
# Create your views here.


def home(request):
    context={}
    dogpuppyy=Puppy.objects.all()
    context['dogpuppy']=dogpuppyy
    return render(request,'dogpuppy/dogpuppy.html',context)

def product_details(request):
    context={}
    if request.method =='POST':
        pid=request.POST.get('did')
        puppyy=Puppy.objects.filter(id = pid)
        context['product']=puppyy
    return render(request,'dogpuppy/product_details.html',context)