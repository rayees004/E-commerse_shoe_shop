from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib import messages
from django.http import HttpResponse

from cart.models import Cart_Order_Summary, Item, Cart
from .models import *
from accounts.models import User,Address

# Create your views here.
def home(request,c_slug=None): #Home page function product view and product category based ffilters
    c_page = None
    products_list = None
    user = None

    user_id = request.session.get('lid')# user_id Session ['lid'] key value storing user
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None

    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(CATEGORY=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    cat = Category.objects.all()
    paginator = Paginator(products_list, 2)
    try:
        page = int(request.GET.get('page', '1'))
    except (ValueError, TypeError):
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'pr': products, 'cat': cat, 'pg': products, 'user': user})

def details(request,c_slug,p_slug):#Product Details Function

    p_details = Product.objects.get(CATEGORY__slug=c_slug, slug=p_slug)
    try:
        user_id = request.session['lid']
        user = User.objects.get(id = user_id)
    except:
        user = None

    return render(request,'details.html',{'de':p_details,'user':user})

def searching(request): #product Search function
    prod=None
    query=None
    print ('this searching')
    if 'q' in request.GET :
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__icontains= query)|Q(desc__icontains= query))
        cat = Category.objects.all()

    return render(request,'index.html',{'pg':prod,'qr':query,'cat':cat,})


def buy_now(request,pr_id): # induvidual product buynow funcition

    product = Product.objects.get(id=pr_id)
    payment_type = True
    if request.method == 'POST':
        user_id = request.session['lid']
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']
        pin = request.POST['pin']
        state = request.POST['state']
        district = request.POST['district']
        place = request.POST['place']
        pay_type = request.POST['payment_type']
        if pay_type == 'cash':
            payment_type = False
        if pay_type == 'pay':
            payment_type = True
        landmark = request.POST['landmark']

        ad = Address.objects.create(
            USER_id=user_id,
            name= name,
            address= address,
            contact=contact,
            pincode=pin,
            state=state,
            district=district,
            place=place,
            landmark=landmark,
        )
        ad.save()
        adress_data = ad
        product_data = Product.objects.get(id=product.id)  # assuming you have product_id

        order_data = Order_Summary.objects.create(
            ADDRESS =adress_data,
            PRODUCT =product_data,
            status='pending',
            price = product_data.price,
            payment_type = payment_type,
        )

        order_data.save()
        return redirect('/')
    try:
        print('---try block user login----------------------------------------------')

        user_id = request.session['lid']
        if user_id == None:
            print('----------------------------------------------------user not login----------------------------------------------')

            return redirect('login')

        else:
            try:
                address_catch = Address.objects.filter(USER_id = user_id)
                for i in address_catch:
                    address_last = i
                if address_last :
                
                    
                
                    return render(request,'order_adress.html',{'product':product,'address':address_last})
                else:
                    return render(request,'order_adress.html',{'product':product})
            except:
                print('---exeption address not found----------------------------------------------')
                return render(request,'order_adress.html',{'product':product})
    except:
        print('---exeption user not login----------------------------------------------')
        return redirect('login')


def order_details(request):
    user_id = request.session['lid']
    user = User.objects.get(id=user_id)
    order_items = Order_Summary.objects.filter(ADDRESS__USER_id = user_id).order_by('-date')
    return render(request,'order_details.html',{'order_items':order_items,'user':user})

def cart_order_address(request,pk):

    
    if request.method == 'POST':
        payment_type = True
        user_id = request.session['lid']
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']
        pin = request.POST['pin']
        state = request.POST['state']
        district = request.POST['district']
        place = request.POST['place']
        pay_type = request.POST['payment_type']
        if pay_type == 'cash':
            payment_type = False
        if pay_type == 'pay':
            payment_type = True
        landmark = request.POST['landmark']

        ad = Address.objects.create(
            USER_id=user_id,
            name=name,
            address=address,
            contact=contact,
            pincode=pin,
            state=state,
            district=district,
            place=place,
            landmark=landmark,
        )
        ad.save()


        
        return redirect('/')



    return render(request,'cart_order_address.html')