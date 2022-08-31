from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model

from .forms import CreateCategoryForm, CreateProductsForm
from .models import Category, Product
import os
from django.contrib.auth.models import User

User = get_user_model()


@permission_required('is_staff')
def manageCategoryPage(request):

    form = CreateCategoryForm
    if request.method == "POST":
        form = CreateCategoryForm(request.POST, request.FILES)
        
        if form.is_valid():
            #print("Is valid")
            form.save()
            return redirect('manage-category')

    category_list = Category.objects.all()
    context = {'form': form, 'category_list':category_list}
    #context = {'form': form}
    return render(request, 'staff-pages/manage-category.html', context)

### Delete item from category
@permission_required('is_staff')
def delete_category(request, c_id):
    queryset = Category.objects.get(pk=c_id)
    if queryset.c_img:
        queryset.c_img.delete()
    queryset.delete()
    return redirect('manage-category')

### Edit/Update category
@permission_required('is_staff')
def edit_category(request, c_id):
    category = Category.objects.get(pk=c_id)

    form = CreateCategoryForm(instance=category)

    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage-category')

        else:
            return HttpResponse('Failed to update')

    context ={'form':form, 'category':category}
    return render(request,'staff-pages/edit-category.html', context)


#Manage Product 
@permission_required('is_staff')
def manage_product(request):
    form = CreateProductsForm
    if request.method == "POST":
        form = CreateProductsForm(request.POST, request.FILES)
        
        if form.is_valid():
            #print("Is valid")
            form.save()
            return redirect('manage-products')

    products = Product.objects.all()
    category = Category.objects.all()
    context = {'form':form, 'products':products, 'category':category}
    return render(request, 'staff-pages/manage-products.html', context)
    

### Delete products
@permission_required('is_staff')
def delete_products(request, p_id):
    queryset = Product.objects.get(pk=p_id)
    if queryset.p_image:
        queryset.p_image.delete()
    queryset.delete()
    return redirect('manage-products')

### Edit/Update products
@permission_required('is_staff')
def edit_products(request, p_id):
    product = Product.objects.get(pk=p_id)
    category = Category.objects.all()

    form = CreateProductsForm(instance=product)

    if request.method == 'POST':
        form = CreateProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage-products')



    context ={'form':form, 'product':product, 'category':category}
    return render(request,'staff-pages/edit-products.html', context)

### Manage Customer
@permission_required('is_staff')
def manage_customers(request):
    customer_list = User.objects.filter(is_staff=False).order_by('-id')
    context = {'customers':customer_list}
    return render(request, 'staff-pages/manage-customers.html', context)


### Manage Staffs
@permission_required('is_staff')
def manage_staffs(request):
    staff_list = User.objects.filter(is_staff=True).order_by('-id')
    context = {'staffs':staff_list}
    return render(request, 'staff-pages/manage-staffs.html', context)

