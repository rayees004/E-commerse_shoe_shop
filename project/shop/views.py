from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage


from .models import *

# Create your views here.
def home(request,c_slug=None):
    c_page = None
    product = None
    if c_slug != None :
        c_page = get_object_or_404(Category, slug=c_slug)
        print(c_page)
        pr = Product.objects.filter(CATEGORY=c_page, available=True)
        print(pr)
    else:
        pr = Product.objects.all().filter(available = True)

    cat = Category.objects.all()
    paginator = Paginator(pr,2)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro = paginator.page(paginator.num_pages)





    return render(request,'index.html',{'pr':pr,'cat':cat,'pg':pro})

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

    return render(request,'index.html',{'pg':prod,'qr':query,'cat':cat})

