from django.shortcuts import render
from .models import Premium
# Create your views here.

def home(request):
    context={}
    premiumm=Premium.objects.all()
    print(premiumm)
    context['dogpremium']=premiumm
    return render(request,'dogpremium/dogpremium.html',context)

def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        premiumm=Premium.objects.filter(id = pid)
        context['product']=premiumm
    return render(request,'dogpremium/product_details.html',context)