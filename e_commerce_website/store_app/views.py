from django.shortcuts import render

from manage_store.models import Category, Product
from django.contrib.auth.decorators import login_required, permission_required

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

def filter_shop(request, id):
    category = Category.objects.all().order_by('c_name')
    #products = Product.objects.all().order_by('id')
    p = Product.objects.filter(p_category_id = id)
    context ={'p':p, 'category':category}
    return render(request, 'pages/filter-shop.html', context)

def product_detail(request, p_id):
    product_detail = Product.objects.get(id=p_id)

    context = {'pd':product_detail}
    return render(request, 'pages/detail.html', context)


@login_required(login_url='login')
def cartPage(request):
    return render(request, 'pages/cart.html')