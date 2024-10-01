# products/admin.py
from django.contrib import admin
from .models import Category, Product # new

admin.site.register(Category) # new
#admin.site.register(Product)  # new
@admin.register(Product) # new 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','featured','price','category') # new
