

from .models import Order, OrderProduct
from django.core.exceptions import ObjectDoesNotExist
def total_cart_products(request):
    
    if request.user.is_authenticated:
        customer = request.user.id
        try:
            order = Order.objects.get(customer=customer)
            if order:
                order_products = OrderProduct.objects.filter(order=order)
                quantity = sum([product.quantity for product in order_products])

            else:
                quantity = 0
        except ObjectDoesNotExist:
            order = None

            
    else:
        quantity = 0

    return {'total_products': quantity}