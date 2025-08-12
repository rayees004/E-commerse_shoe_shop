
from django.urls import path
from .import views
from accounts.views import login



urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/', views.home, name='cat_pr'),
    path('accounts/login/<slug:c_slug>',login,name='cat_pr_log'),
    path('<slug:c_slug>/<slug:p_slug>/', views.details, name='details'),
    path('search',views.searching,name='search'),

]

