from django.urls import path
from .import views

urlpatterns = [
    path('cart_details',views.cart_details,name='cart_details'),
    path('add/<int:product_id>/',views.cart_add,name='add_cart'),
    path('min_cart/<int:product_id>/',views.cart_min,name='min_cart'),
    path('remove_item/<int:product_id>/',views.cart_remove,name='remove_item'),
]