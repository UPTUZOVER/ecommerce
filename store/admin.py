
from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category','image', 'modified_date', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)























