from django.db import models
from category.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Maxsulot nomi', unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='Slug for the category' )
    description = models.TextField(verbose_name='Description nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    image = models.ImageField(upload_to='prod_image/product_image')
    chegirma = models.IntegerField(null=True, blank=True,default=0,
                                    validators=[
                                        MinValueValidator(0,
                                                          message='Satish mikdori 0 yoki undan katta bo\'lishi kerak.'),
                                         MaxValueValidator(100,
                                                             message='Sotish mikdori 100 yoki undan kam bo\'lishi kerak.')],)
    stock = models.IntegerField(verbose_name='Sotish Mikdori', help_text='Maxsulot soni')
    true_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0, verbose_name='Haqiqiy narx')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category nomi')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
        
    def save(self, *args, **kwargs):

        if self.chegirma is not None and self.price is not None:
            total = self.price - (self.price * self.chegirma / 100)
            self.true_price = total
        super().save(*args, **kwargs)
        
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/path/to/default/image.jpg'

    def get_discounted_price(self):
        if self.chegirma is not None and self.price is not None:
            discounted_price = self.price - (self.price * self.chegirma / 100)
            return discounted_price
        return None


    def get_formatted_discount(self):
        if self.chegirma is not None:
            return f"{self.chegirma}%"

        return None


    def get_formatted_created_date(self):
        return self.created_date.strftime('%Y-%m-%d')

    def get_formatted_modified_date(self):
        return self.modified_date.strftime('%Y-%m-%d')
    
    
