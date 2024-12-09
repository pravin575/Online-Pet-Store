from django.shortcuts import render
from .models import  Veg
# Create your views here.

def home(request):
    context={}
    dogvegg=Veg.objects.all()
    print(dogvegg)
    context['dogveg']=dogvegg
    return render(request,'dogveg/dogveg.html',context)

def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        vegg=Veg.objects.filter(id = pid)
        context['product']=vegg
    return render(request,'dogveg/product_details.html',context)