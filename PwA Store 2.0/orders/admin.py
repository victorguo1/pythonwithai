from django.contrib import admin
from . models import Order,OrderItem

@admin.register(Order) # new 
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','orderdate','shippingdate') # new

@admin.register(OrderItem) # new 
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','item','quantity','price') # new
