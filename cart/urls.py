from django.urls import path
from .views import *
from ecommece_moon.settings import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add_product/<int:product_id>/', add_cart, name='add_cart'),
    path('sub_product/<int:product_id>/', sub_cart, name='sub_cart'),
    path('delete/<int:product_id>/', remove_cart, name='delete_cart_item'),

]




