from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def home(request,c_slug=None):
    c_page = None
    product = None
    if c_slug != None :
        c_page = get_object_or_404(Category, slug=c_slug)
        pr = Product.objects.filter(CATEGORY=c_page, available=True)
    else:

        pr = Product.objects.all().filter(available = True)
    cat = Category.objects.all()
    return render(request,'index.html',{'pr':pr,'cat':cat})

def details(request):
    print('this is the details')
    return render(request,'details.html')