from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date', 'modified_date']
    readonly_fields = ['created_date', 'modified_date']

    def clear_cart(self, request, queryset):
        for cart in queryset:
            cart.clear_cart()
    clear_cart.short_description = 'Clear Cart'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'cart', 'quantity', 'is_active', 'created_date', 'modified_date']
    list_filter = ['is_active']
    search_fields = ['product__name', 'cart__id']
    actions = ['toggle_active', 'increment_qutrap adventure 2 antity', 'decrement_quantity']

    def toggle_active(self, request, queryset):
        for item in queryset:
            item.toggle_active()
    toggle_active.short_description = 'Toggle Active Status'

    def increment_quantity(self, request, queryset):
        for item in queryset:
            item.increment_quantity()
    increment_quantity.short_description = 'Increment Quantity'

    def decrement_quantity(self, request, queryset):
        for item in queryset:
            item.decrement_quantity()
    decrement_quantity.short_description = 'Decrement Quantity'

    def get_subtotal_price(self, obj):
        return obj.get_subtotal_price()
    get_subtotal_price.short_description = 'Subtotal Price'

    def is_in_stock(self, obj):
        return obj.is_in_stock()
    is_in_stock.boolean = True
    is_in_stock.short_description = 'In Stock'