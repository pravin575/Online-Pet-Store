from django.shortcuts import render
from .models import Iteams
# Create your views here.

def home(request):
    context={}
    dogwett=Iteams.objects.all()
    print(dogwett)
    context['dogwet']=dogwett
    return render(request,'dogwet/dogwet.html',context)
    
def product_details(request):
    context={}
    if request.method =='POST':
        pid=request.POST.get('did')
        iteam=Iteams.objects.filter(id = pid)
        context['product']=iteam
    return render(request,'dogwet/product_details.html',context)