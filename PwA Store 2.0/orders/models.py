 # PwA 2.0
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 
from products.models import Product

# Get the user model
User = get_user_model()

class Order(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderdate = models.DateTimeField(auto_now_add=True)
    shippingdate = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    address = models.CharField(max_length=200, verbose_name='Address')
    city = models.CharField(max_length=50, verbose_name='City')
    province = models.CharField(max_length=50, verbose_name='Province')
    postalcode = models.CharField(max_length=7, verbose_name='Postal Code')

    def __str__(self):
        return self.orderdate.strftime("%b.%d,%Y,%I:%M %p")   
    
    def get_absolute_url(self):  
        return reverse('mainapp:home') #,args=[str(self.pk)])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.item.name  