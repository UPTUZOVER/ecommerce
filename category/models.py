from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Category nomi', unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='descriptions nomi')
    image = models.ImageField(upload_to='category_images', blank=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='Slug for the category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']
        verbose_name = 'category'

    def get_url(self):
        return reverse("product_slug", args=[self.slug])

    def get_absolute_url(self):
        return reverse("category_detail", args=[self.slug])

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/path/to/default/image.jpg'


    def get_total_products(self):
        return self.get_products().count()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    