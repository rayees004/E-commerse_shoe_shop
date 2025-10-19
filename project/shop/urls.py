
from django.urls import path
from .import views
from accounts.views import login



urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/', views.home, name='cat_pr'),
    path('<slug:c_slug>/<slug:p_slug>/', views.details, name='details'),
    path('buy_now/<int:pr_id>',views.buy_now,name='buy_now'),
    path('cart_order_address/<pk>',views.cart_order_address,name='cart_order_address'),
    path('order_details',views.order_details,name='order_details'),
    path('search',views.searching,name='search'),

]

