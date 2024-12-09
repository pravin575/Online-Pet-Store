from django.shortcuts import render
from .models import Bake
# Create your views here.

def home(request):
    context={}
    dogbakee=Bake.objects.all()
    print(dogbakee)
    context['dogbake']=dogbakee
    return render(request,'dogbake/dogbake.html',context)

def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        bakee=Bake.objects.filter(id = pid)
        context['product']=bakee
    return render(request,'dogbake/product_details.html',context)
