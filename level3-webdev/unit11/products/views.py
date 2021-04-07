# products/views.py
from django.views.generic import ListView #new
from .models import Product #new

class Home(ListView): # new
    model = Product
    context_object_name = "all_products_list"
    template_name = "products/home.html"
