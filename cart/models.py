from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class Cart(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    session_id = models.CharField(max_length=3000, 
                                    blank=True, 
                                    null=True, 
                                    default=" ")

    def is_empty(self):
        return self.cartitem_set.count() == 0

    def clear_cart(self):
        self.cartitem_set.all().delete()

    def get_item_count(self):
        return self.cartitem_set.count()

    def remove_item(self, cart_item_id):
        try:
            cart_item = self.cartitem_set.get(id=cart_item_id)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass

    def update_item_quantity(self, cart_item_id, quantity):
        try:
            cart_item = self.cartitem_set.get(id=cart_item_id)
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
        except CartItem.DoesNotExist:
            pass
            
        
        
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def toggle_active(self):
        self.is_active = not self.is_active
        self.save()

    def increment_quantity(self):
        self.quantity += 1
        self.save()

    def decrement_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()

    def get_subtotal_price(self):
        return self.product.price * self.quantity

    

    def is_in_stock(self):
        return self.product.stock >= self.quantity
    
    
    
    