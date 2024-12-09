from django.shortcuts import render
from .models import Catwet
# Create your views here.

def home(request):
    context={}
    catwett=Catwet.objects.all()
    print(catwett)
    context['catwet']=catwett
    return render(request,'catwet/catwet.html',context)


def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        catwett=Catwet.objects.filter(id = pid)
        context['product']=catwett
    return render(request,'catwet/product_details.html',context)