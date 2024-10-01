# products/urls.py
from django.urls import path
from . views import Home,ProductListView
from cart.views import add_to_cart, CartListView, increase_cart, decrease_cart #new
from orders.views import OrderCreateView,OrderCompleteView # PwA 2.0
app_name= 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/<category>', ProductListView.as_view(), name='products'), # PwA 2.0
    path('cart/<slug>', add_to_cart, name='cart'),  
    path('increase/<slug>', increase_cart, name='increase-cart'),  
    path('decrease/<slug>', decrease_cart, name='decrease-cart'),  
    path('cart/', CartListView.as_view(), name='cart-home'),  
    path('orders/new/', OrderCreateView.as_view(), name='create-order'),
    path('orders/complete/<int:pk>', OrderCompleteView.as_view(),name='complete-order'),
]