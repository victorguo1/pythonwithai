# products/views.py
from django.views.generic import ListView #new
from .models import Product,Category #new

class Home(ListView):
    model = Product
    context_object_name = 'all_products_list'
    template_name = 'products/home.html'

    def get_queryset(self):  # PwA 2.0
        return Product.objects.filter(featured = True)

class ProductListView(ListView): # PwA 2.0 
    model = Product
    context_object_name = 'all_products_list'
    template_name = 'products/products.html'

    def get_queryset(self):
        categoryid = Category.objects.get(title=self.kwargs['category'])
        return Product.objects.filter(category=categoryid)