#  PwA 2.0
from datetime import datetime, timedelta
from django.shortcuts import render, redirect # new
from django.forms import ModelForm # new
from django.views.generic.edit import CreateView # new
from django.views.generic import DetailView # new 
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Order, OrderItem  
from cart.models import Cart 

class OrderCreateForm(ModelForm):    
    class Meta:
        model = Order
        fields = ['address','city','province','postalcode']

class OrderCreateView(LoginRequiredMixin,CreateView):  
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['cart_list'] = Cart.objects.filter(user=self.request.user)
        return context

    def post(self, request):
        form = self.form_class(request.POST)  
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.orderdate = datetime.now()
            form.instance.shippingdate = form.instance.orderdate + timedelta(days=3)
        
            form.save()
            #move cart into order items
            cart_qs = Cart.objects.filter(user=self.request.user)
            if cart_qs.exists():
                for cart in cart_qs:
                    if cart.quantity > 0:
                        order_item,created = OrderItem.objects.get_or_create(
                            order=form.instance,
                            item=cart.item,
                            defaults={'quantity': 0,'price':0},)

                        order_item.order = form.instance
                        order_item.item = cart.item
                        order_item.quantity = cart.quantity
                        order_item.price = cart.item.price
                        order_item.save()
                        cart.delete()                        
            return redirect('mainapp:complete-order',pk=order_item.order.pk)
        return render(request, 'order_create.html', {'form': form})

class OrderCompleteView(LoginRequiredMixin,DetailView): # PwA 2.0
    model = Order
    context_object_name = "order"
    template_name = 'orders/order_complete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        order = Order.objects.get(pk=self.kwargs['pk'],user=self.request.user)
        context['order_list'] = OrderItem.objects.filter(order=order)
        return context