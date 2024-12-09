from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    context={}
    shopee=Product.objects.all()
    print(shopee)
    context['shop']=shopee
    return render(request,'shop/home.html',context)

def search(request):
    context={}
    if request.method=='POST':
        productname=request.POST['productname']
        print(productname)
        product=Product.objects.filter(product_name__contains=productname)
        context['product']=product
    return render(request,'shop/search.html',context)


def product_details(request):
    context = {}
    if request.method == 'POST':
        pid = request.POST.get('did')
        products = Product.objects.filter(id = pid)
        context['products'] = products
    return render(request,'shop/product_details.html',context)