from django.contrib import admin
from .models import *

@admin.register(Ulchamlar)
class UlchlarAdmin(admin.ModelAdmin):
    list_display = ['product', 'ulcham_turlari', 'ulcham_qiymat', 'is_active', 'created_date']
    list_filter = ['product', 'ulcham_turlari', 'ulcham_qiymat', 'is_active', 'created_date']
    search_fields = ['product', 'ulcham_turlari', 'ulcham_qiymat', 'is_active', 'created_date']

