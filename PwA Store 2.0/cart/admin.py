# cart/admin.py
from django.contrib import admin
from .models import Cart # new

#admin.site.register(Cart) # new
@admin.register(Cart) # new 
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','item','quantity') # new