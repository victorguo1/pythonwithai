# cart/views.py
from django.contrib import messages  
from django.shortcuts import render, get_object_or_404, redirect 
from django.views.generic import ListView # new
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart
from products.models import Product 

# Add to Cart View
def add_to_cart(request, slug):
    _increase_cart(request,slug)
    return redirect("mainapp:home")

# Increase quantity in the cart
def increase_cart(request, slug):  # new
    _increase_cart(request,slug)
    return redirect("mainapp:cart-home")

# helper function to increase quantity in the cart      
def _increase_cart(request,slug):
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
        messages.info(request, f"{cart.item.name} quantity has updated.") 

# decrease quantity in the cart
def decrease_cart(request, slug):  # new
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
            messages.info(request, f"{item.name} quantity has updated.") 
        else:
            cart.delete()
            messages.info(request, "This item was removed from your cart.")
    else:
        messages.warning(request, "This item was not in your cart")
    return redirect("mainapp:cart-home")

class CartListView(LoginRequiredMixin,ListView): # new
    model = Cart
    template_name = 'cart/home.html'
    context_object_name = 'cart_list' 

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)