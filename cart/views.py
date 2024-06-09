from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse




def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def cart(request):
    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        total = 0
        for i in cart_items:
            total += i.quantity * i.product.true_price
        
        soliq = (total * 2) / 100
        true_total = total - soliq
    except Cart.DoesNotExist:
        cart_items = []
        total = 0
        soliq = 0
        true_total = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'soliq': soliq, 
        'true_total': true_total
    }
    
    return render(request, 'cart.html', context)


def add_cart(request, product_id):
    color = request.GET["color"]
    size = request.GET["size"]
    return HttpResponse(color+" "+size)
    exit()
    
    product = get_object_or_404(Product.objects.select_related('category'), id=product_id)
    
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


def sub_cart(request, product_id):
    product = get_object_or_404(Product.objects.select_related('category'), id=int(product_id))
    cart = Cart.objects.get(session_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')



def remove_cart(request, product_id):
    product = get_object_or_404(Product.objects.select_related('category'), id=int(product_id))
    cart = Cart.objects.get(session_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)

    cart_item.delete()
    return redirect('cart')




# def delete(request, cart_item_id):
#     
#      cart = Cart.objects.get(session_id=_cart_id(request))
#         cart.remove_item(cart_item_id)
#     except Cart.DoesNotExist:
#         pass
#     return redirect('cart')





































































































































































