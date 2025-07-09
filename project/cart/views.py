from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from shop.models import *
from .models import *

# Create your views here.
def cart_details(request,tot = 0, count = 0,ct_items = None):
    try:
        ct = Cart.objects.get(cart_id=c_id(request))
        ct_items = Item.objects.filter(CART=ct,active=True)
        for i in ct_items:
            tot +=(i.PRODUCT.price * i.quntity)
            count += i.quntity
    except ObjectDoesNotExist:
        pass

    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def cart_add(request,product_id):
    prod = Product.objects.get(id = product_id)
    try:
        ct = Cart.objects.get(cart_id=c_id(request))
    except Cart.DoesNotExist:
        ct = Cart.objects.create(cart_id = c_id(request))
        ct.save()
    try:
        # c_item = Item.objects.get(PRODUCT=prod,quntity=1,CART=ct)
        c_item = Item.objects.get(PRODUCT=prod,CART=ct)
        if c_item.quntity < c_item.PRODUCT.stock :
            c_item.quntity = c_item.quntity + 1
            c_item.save()
    except Item.DoesNotExist:
        c_item = Item.objects.create(PRODUCT=prod,quntity = 1,CART = ct)
        c_item.save()
    return redirect('cart_details')



def cart_min(request):
    pass