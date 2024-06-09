from django.contrib import admin
from .models import Wishlist, Wishlist_Item

class Wishlist_ItemInline(admin.TabularInline):
    model = Wishlist_Item
    extra = 0

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'created_date', 'modified_date', 'total_items')
    search_fields = ('session_id',)
    inlines = [Wishlist_ItemInline]

@admin.register(Wishlist_Item)
class Wishlist_ItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'wishlist', 'created_at', 'updated_at')
    search_fields = ('product__name', 'wishlist__session_id')
    list_filter = ('wishlist', 'created_at', 'updated_at')