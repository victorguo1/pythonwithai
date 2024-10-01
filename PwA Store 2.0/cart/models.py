# cart/models.py
from django.db import models
from django.contrib.auth import get_user_model #new
from products.models import Product #new

# Get the user model
User = get_user_model()

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    # Getting the total price for an item
    def get_total(self):
        total = self.item.price * self.quantity
        return total

    # Get total quantity for all items in a cart
    @classmethod
    def get_cart_quantity(cls,user):
        total_quantity = 0

        items = Cart.objects.filter(user=user)
        if items.exists():
            for item in items:
                total_quantity += item.quantity
    	
        return total_quantity

    # Get total price of the cart
    @classmethod
    def get_cart_sum(cls,user):
        sum = 0.0

        items = Cart.objects.filter(user=user)
        if items.exists():
            for item in items:
                sum += item.get_total()
    	
        return sum
