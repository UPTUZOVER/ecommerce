from .views import _wishlist_id
from .models import Wishlist, Wishlist_Item

def sanash_uchun_samur(request):
    wishlist_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            wishlist = Wishlist.objects.get(session_id=_wishlist_id(request))
            wishlist_items = Wishlist_Item.objects.filter(wishlist=wishlist)
            for item in wishlist_items:
                wishlist_count += 1  # Changed from `item.count` to `1` since there is no `count` field
        except Wishlist.DoesNotExist:
            wishlist_count = 0
    return {
        'wishlist_count': wishlist_count,
    }