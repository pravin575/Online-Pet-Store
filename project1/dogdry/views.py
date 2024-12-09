from django.shortcuts import render
from .models import Item
from django.contrib.auth.models import User
from cart.models import Cart
from django.shortcuts import redirect

# Create your views here.

def home(request):
    context={}
    dog=Item.objects.all()
    print(dog)
    context['dogdry']=dog
    return render(request,'dogdry/dogdry.html',context)


def search(request):
    context={}
    if request.method=='POST':
        Productname=request.POST['iteamname']
        product=Item.objects.filter(item_name__contains=Productname)
        print(product)
        context['product']=product
    return render(request,'dogdry/search.html',context)

def product_details(request):
    context={}
    if request.method=='POST':
        pid=request.POST.get('did')
        item=Item.objects.filter(id = pid)
        context['product']=item
    return render(request,'dogdry/product_details.html',context)




def cart(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        print(pid)
        print(request.session.get('username'))
        username = User.objects.get(username = request.session.get('username'))
        print(username)
        name = Item.objects.get(id = pid)
        print(name)
        product = Item.objects.filter(id = pid)
        print(product)
        productc = Cart.objects.filter(name = name,username__username = username)
        print(productc)
        if productc:
            for i in productc:
                quantity = i.quantity + 1
                total_price = i.price * quantity
            Cart.objects.filter(name = name,username__username=username).update(quantity = quantity,total_price = total_price)
        else:
            for i in product:
                price = i.product_price
                desc = i.product_desc
                image = i.product_image
            mycart = Cart.objects.create(username = username,name = name,price = price,desc = desc,image = image,total_price = price,quantity = 1)
            mycart.save()
    return redirect('home')


def showcart(request):
    username = request.session.get('username')
    print(username)
    context = {}
    products = Cart.objects.filter(username__username = username)
    print(products)
    context['products'] = products
    return render(request,'cart/cart.html',context)

