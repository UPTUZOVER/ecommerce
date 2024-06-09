from django.urls import path
from . import views

urlpatterns = [
    path('', views.asosiy, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]