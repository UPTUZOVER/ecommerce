from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('-created_date')
        # p = Paginator(products, 1)
        # page_number = request.GET.get('page')
        # page_obj = p.get_page(page_number)  

    else:
        products = Product.objects.filter(is_available=True)
      #  p = Paginator(products, 1)
     #   page_number = request.GET.get('page')
      # # page_obj = p.get_page(page_number)  

    
    
    category = Category.objects.all()
    context = {
       # 'page_obj':page_obj,
        'products': products,
        'product_count': products.count(),
        'categories': category,
    }
    return render(request, 'store.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    except Exception as e:
        raise e
    
    
    context = {
        'product': product,
    }
    return render(request, "product_detail.html", context)

    



















