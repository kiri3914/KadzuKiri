from django.contrib import admin

from django.contrib import admin


from .models import Product, ProductImage, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'category', 'price', 'is_available', 'created_at', 'date_expired', 'base_image')
    list_filter = ('created_at', 'price', 'is_available')
    list_per_page = 10
    search_fields = ('name', 'description', 'category')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    list_per_page = 10
    search_fields = ('title', 'description')

admin.site.register(Category, CategoryAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','image')
    list_per_page = 10

admin.site.register(ProductImage, ProductImageAdmin)


