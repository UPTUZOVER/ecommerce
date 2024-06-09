from django.db import models
from store.models import Product









    
ulcham_turlarini_tanlash = (
    ('color ', 'color'),
    ('size', 'size'),

)    


class Ulchamlar(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ulcham_turlari = models.CharField(max_length=20, choices=ulcham_turlarini_tanlash)
    ulcham_qiymat = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.ulcham_turlari}: {self.ulcham_qiymat}"

    def __unicode__(self):
        return self.product