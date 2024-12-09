from django.shortcuts import render
from .models import Cart
from shop.models import Product
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.


def cart(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        print(pid)
        print(request.session.get('username'))
        username = User.objects.get(username = request.session.get('username'))
        print(username)
        name = Product.objects.get(id = pid)
        print(name)
        product = Product.objects.filter(id = pid)
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

def deletefromcart(request):
    # username=request.session.get('username')
    if request.method=="POST":
        cid=request.POST.get('cid')
        print(cid)
        # item=Item.objects.get(item_name=Pname)
        # print(item)
        items=Cart.objects.get(id = cid)
        print("Deleted")
        items.delete()
    # context={}
    # itemss=Cart.objects.filter(username__username=username)
    # context['items']=items
    return redirect('showcart')
    

