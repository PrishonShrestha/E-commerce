from django.db import models
from user_mgmt.models import User
from manage_store.models import Product



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    o_date = models.DateTimeField(auto_now_add=True)
    o_status = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_products = self.orderproduct_set.all()
        cart_total = sum([product.get_total for product in order_products])
        return cart_total

    @property
    def get_cart_products(self):
        order_products = self.orderproduct_set.all()
        total_products = sum([product.quantity for product in order_products])
        return total_products


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.price * self.quantity
        return total

class ShippingDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    s_full_name = models.CharField(max_length=100)
    s_email = models.EmailField(max_length=100)
    s_contact = models.CharField(max_length=20)
    s_address = models.CharField(max_length=100)

    def __str__(self):
        return self.s_full_name


