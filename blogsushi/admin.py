from django.contrib import admin
from .models import Product, ProductCategory


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'created', 'edited', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
