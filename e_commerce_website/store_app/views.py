from django.shortcuts import render, redirect

from store_app.forms import ShippingDetailsForm, UpdateOrderForm
from .models import Order, OrderProduct, ShippingDetails
from manage_store.models import Category, Product
from django.contrib.auth.decorators import login_required, permission_required

from django.http import JsonResponse
from user_mgmt.decorators import unauthenticated_user

import json
from django.db.models import Count, Q


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
    products = Product.objects.filter(p_category_id = id)
    context ={'category':category, 'products':products}
    return render(request, 'pages/shop.html', context)

# View Product details
def product_detail(request, p_id):
    product_detail = Product.objects.get(id=p_id)
    #print(product_detail.p_category_id)
    related_products = Product.objects.filter(p_category_id=product_detail.p_category_id)[:4]

    context = {'pd':product_detail, 'related_products':related_products}
    return render(request, 'pages/detail.html', context)


@login_required(login_url='login')
def cartPage(request):
    if request.user.is_authenticated:
        customer = request.user.id
        order, created = Order.objects.get_or_create(customer_id = customer, o_placed=False)
        #order, created = Order.objects.get_or_create(Q(customer_id = customer) & Q(o_placed=False))
        products = order.orderproduct_set.all()
        print(order)
        print(products)

    else:
        products = []
        order = {'get_cart_total':0, 'get_cart_products':0}

    context = {'products':products, 'order':order}

    return render(request, 'pages/cart.html', context)


# Update cart products
def updateProduct(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('ProductId: ', productId)

    customer = request.user.id
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer_id = customer, o_placed=False)
    #order, created = Order.objects.get_or_create(Q(customer_id = customer) & Q(o_placed=False))
    
    orderProduct, created = OrderProduct.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderProduct.quantity = (orderProduct.quantity + 1)
    elif action == 'remove':
        orderProduct.quantity = (orderProduct.quantity - 1)

    orderProduct.save()

    if orderProduct.quantity <= 0:
        orderProduct.delete()

    return JsonResponse('Item was added', safe=False)


#Checkout page
@login_required
def checkoutPage(request, o_id):
    orderID = Order.objects.get(id=o_id)
    
    form = ShippingDetailsForm
    orderForm = UpdateOrderForm(instance=orderID)
    


    if request.method == "POST":
        form = ShippingDetailsForm(request.POST)
        orderForm = UpdateOrderForm(request.POST, instance=orderID)
        
        
        if form.is_valid() and orderForm.is_valid():
            form.save()
            orderForm.save()
            # print("hello")
            

            return redirect('home')
        # print('Success')
        

    customer = request.user.id
    print(customer)
    order, created = Order.objects.get_or_create(customer_id = customer, o_placed=False)
    #order, created = Order.objects.get_or_create(Q(customer_id = customer) & Q(o_placed=False))
    products = order.orderproduct_set.all()


    context = {'products':products, 'order':order, 'form':form, 'orderForm':orderForm}
    return render(request, 'pages/checkout.html', context)



def myOrdersPage(request, c_id):

    orders = Order.objects.filter(Q(customer_id=c_id) & Q(o_placed=True) & ~Q(o_status="Delivered"))
    
    # product = orders.orderproduct_set.all()
    print(orders)
    
    context={'orders':orders}
    return render(request, 'pages/my-orders.html', context)
    

