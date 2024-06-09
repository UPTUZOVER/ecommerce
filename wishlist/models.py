from django.db import models
from store.models import Product
from django.utils import timezone

class Wishlist(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    session_id = models.CharField(max_length=3000, blank=True, null=True, default="")

    def __str__(self):
        return f"Wishlist {self.session_id}"

    def add_item(self, product):
        item, created = Wishlist_Item.objects.get_or_create(wishlist=self, product=product)
        self.modified_date = timezone.now()
        self.save()
        return item

    def remove_item(self, product):
        item = Wishlist_Item.objects.filter(wishlist=self, product=product).first()
        if item:
            item.delete()
            self.modified_date = timezone.now()
            self.save()

    def clear(self):
        Wishlist_Item.objects.filter(wishlist=self).delete()
        self.modified_date = timezone.now()
        self.save()

    @property
    def total_items(self):
        return Wishlist_Item.objects.filter(wishlist=self).count()

class Wishlist_Item(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} in {self.wishlist.session_id}"

    def save(self, *args, **kwargs):
        self.wishlist.modified_date = timezone.now()
        self.wishlist.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.wishlist.modified_date = timezone.now()
        self.wishlist.save()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('wishlist', 'product')
        verbose_name = 'Wishlist Item'
        verbose_name_plural = 'Wishlist Items'
