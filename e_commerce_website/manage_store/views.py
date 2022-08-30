from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required

from .forms import CreateCategoryForm, CreateProductsForm
from .models import Category, Product
import os


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
        else:
            return HttpResponse("Failed to add product")

    products = Product.objects.all()
    category = Category.objects.all()
    context = {'form':form, 'products':products, 'category':category}
    return render(request, 'staff-pages/manage-products.html', context)
    



