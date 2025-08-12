from django.shortcuts import render, redirect, get_object_or_404
from shop import views


# Create your views here.
from accounts.models import User
from shop.views import home


def register(request):


    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            confirm_pass = True

            if not User.objects.filter(username = uname).exists():
                n_user =User(
                    fname= fname,
                    lname= lname,
                    username= uname,
                    email= email,
                    password= password1

                )
                n_user.save()


                # print('your username is valid')
                return redirect('login')

            else:
                # print('your username is not valid')
                v_uname = False
                return render(request,'registration.html',{'v_uname':v_uname})

        else:
            confirm_pass = False
            return render(request, 'registration.html', {'pass':confirm_pass})

    return render(request,'registration.html',)
def login(request,c_slug=None):
    if request.method == 'POST':
        uname = None
        password = None
        user_id = None
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user_id = request.POST.get('user_id')
        print('--------------------------user_id',user_id)
        if (uname != None and password != None):

            user = User.objects.filter(username=uname, password=password)
        else:
            user = User.objects.filter(id=user_id)


        if user.exists():
              from shop.models import Product,Category
              pro = Product.objects.all()
              cat = Category.objects.all()
              return render(request,'index.html',{'user':user,'pg':pro,'cat':cat})

    return render(request,'login.html')

def logout(request):
    return redirect('/')

