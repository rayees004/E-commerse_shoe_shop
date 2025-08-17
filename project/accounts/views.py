from django.shortcuts import render, redirect, get_object_or_404
from shop import views


# Create your views here.
from accounts.models import User
from shop.views import home


def register(request):
    print('------------------------------------------------------------------------------------------------not resppond')
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
    return render(request,'registration.html')
def login(request,c_slug=None):
    if request.method == 'POST':

        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=uname, password=password)

        if user.exists():
            log = User.objects.get(username=uname, password=password)
            request.session['lid'] = log.id
            return redirect('/')

    return render(request,'login.html')

def logout(request):
    request.session['lid'] = None
    return redirect('/')

