from django.shortcuts import render, redirect
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
def login(request):
    if request.method == 'POST':
        print('working the post method')
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=uname, password=password)
        ge = home(request)


        if user:
            # return redirect('/',)
            return render(request, 'index.html', {'pr': ge.pr, 'cat': ge.cat, 'pg': ge.pro,'user':user})
        else:
            return redirect('login')
    return render(request,'login.html')

