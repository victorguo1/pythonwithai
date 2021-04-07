# cart/views.py
from django.contrib import messages  
from django.shortcuts import render, get_object_or_404, redirect  
from django.views.generic import ListView # new
from .models import Cart # new
from products.models import Product # new

# Add to Cart View
# Function Based View
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)    
    cart, created = Cart.objects.get_or_create(
                item=item,
                user=request.user,
            ) 

    if created:
        cart.quantity = 1
        cart.save()
        messages.info(request, f"{cart.item.name} has been added to your cart.")
    else:
        cart.quantity +=1
        cart.save()
        messages.info(request, f"{cart.item.name} quantity has been updated.") 

    return redirect("mainapp:home")

# Class Based View
class CartListView(ListView): # new
    model = Cart
    template_name = 'cart/home.html'
    context_object_name = 'cart_list' 

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
