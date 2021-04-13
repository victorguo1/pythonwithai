# cart/admin.py
from django.contrib import admin
from .models import Cart  

#admin.site.register(Cart)
@admin.register(Cart) # new 
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','item','quantity') # new