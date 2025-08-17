from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage



from .models import *
from accounts.models import User

# Create your views here.
def home(request,c_slug=None):
    c_page = None
    products_list = None
    user = None

    user_id = request.session.get('lid')
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

def details(request,c_slug,p_slug):

    p_details = Product.objects.get(CATEGORY__slug=c_slug, slug=p_slug)

    return render(request,'details.html',{'de':p_details})

def searching(request):
    prod=None
    query=None
    print ('this searching')
    if 'q' in request.GET :
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__icontains= query)|Q(desc__icontains= query))
        cat = Category.objects.all()

    return render(request,'index.html',{'pg':prod,'qr':query,'cat':cat,})





