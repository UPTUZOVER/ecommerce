
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Wishlist, Wishlist_Item
from django.http import JsonResponse
from cart.models import Cart, CartItem

def asosiy(request):
    wishlist_id = _wishlist_id(request)
    wishlist, created = Wishlist.objects.get_or_create(session_id=wishlist_id)
    wishlist_items = Wishlist_Item.objects.filter(wishlist=wishlist)
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist.html', context)

def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_id = _wishlist_id(request)

    try:
        wishlist = Wishlist.objects.get(session_id=wishlist_id)
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(session_id=wishlist_id)
        wishlist.save()

    try:
        wishlist_item = Wishlist_Item.objects.get(product=product, wishlist=wishlist)
    except Wishlist_Item.DoesNotExist:
        wishlist_item = Wishlist_Item.objects.create(product=product, wishlist=wishlist)
        wishlist_item.save()
    return redirect('wishlist')

def _wishlist_id(request):
    try:
        wishlist = request.session.session_key
        if not wishlist:
            wishlist = request.session.create()
        return wishlist
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_id = _wishlist_id(request)
    wishlist = get_object_or_404(Wishlist, session_id=wishlist_id)
    wishlist_item = get_object_or_404(Wishlist_Item, wishlist=wishlist, product=product)
    wishlist_item.delete()
    return redirect('/')

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(session_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()
    
    return redirect('cart')

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart