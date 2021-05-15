from django.contrib import admin
from .models import Product

# Register your models here.

#admin.site.register(Article)


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_filter = ('title', 'description', 'product_image', 'price')
    list_display = ('title', 'description', 'product_image', 'price')
