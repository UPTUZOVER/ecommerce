from django.contrib import admin
from .models import *



from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    ordering = ['name']
    fields = ['name', 'description', 'slug', 'image']
    readonly_fields = ['image_preview']
    prepopulated_fields = {'slug': ('name',)}
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" alt="{obj.name}" style="max-height: 200px; max-width: 200px;" />'
        return None

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

admin.site.register(Category, CategoryAdmin)
