from django.shortcuts import render
from .models import Order, OrderProduct, ShippingDetails
from manage_store.models import Category, Product
from django.contrib.auth.decorators import login_required, permission_required

from user_mgmt.decorators import unauthenticated_user

def homePage(request):
    category = Category.objects.all()[:3]
    products = Product.objects.all()[:8]

    context= {'category':category, 'products':products}
    return render(request, 'pages/index.html', context)

def shopPage(request):
    category = Category.objects.all().order_by('c_name')
    products = Product.objects.all().order_by('id')

    context ={'category':category, 'products':products}
    return render(request, 'pages/shop.html', context)

### Search products by category
def filter_shop(request, id):
    category = Category.objects.all().order_by('c_name')
    #products = Product.objects.all().order_by('id')
    p = Product.objects.filter(p_category_id = id)
    context ={'p':p, 'category':category}
    return render(request, 'pages/filter-shop.html', context)

# View Product details
def product_detail(request, p_id):
    product_detail = Product.objects.get(id=p_id)
    #print(product_detail.p_category_id)
    related_products = Product.objects.filter(p_category_id=product_detail.p_category_id)[:4]

    context = {'pd':product_detail, 'related_products':related_products}
    return render(request, 'pages/detail.html', context)


@login_required(login_url='login')
def cartPage(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer_id = customer)
    products = order.orderproduct_set.all()
    #print(products)

    context = {'products':products, 'order':order}
    return render(request, 'pages/cart.html', context)


def checkoutPage(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer_id = customer)
        products = order.orderproduct_set.all()
    else:
        products = []
        order = {'get_cart_total':0, 'get_cart_products':0}
    #print(products)

    context = {'products':products, 'order':order}
    return render(request, 'pages/checkout.html', context)