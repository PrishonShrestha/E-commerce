from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model

from user_mgmt.forms import CreateUserForm, UserUpdateForm

from .forms import CreateCategoryForm, CreateProductsForm
from store_app.forms import UpdateOrderForm
from .models import Category, Product
from store_app.models import Order, OrderProduct, ShippingDetails
from django.db.models import Q
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
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('manage-customers')
    customer_list = User.objects.filter(is_staff=False).order_by('-id')
    context = {'customers':customer_list, 'form':form}
    return render(request, 'staff-pages/manage-customers.html', context)

@permission_required('is_staff')
def delete_customers(request, c_id):
    queryset = User.objects.get(id=c_id)
    queryset.delete()
    return redirect('manage-customers')


### Manage Staffs
@permission_required('is_staff')
def manage_staffs(request):

    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            #print("Is valid")
            form.save()
            return redirect('manage-staffs')
    staff_list = User.objects.filter(is_staff=True).order_by('-id')
    context = {'staffs':staff_list, 'form':form}
    return render(request, 'staff-pages/manage-staffs.html', context)

@permission_required('is_staff')
def delete_staffs(request, s_id):
    queryset = User.objects.get(id=s_id)
    queryset.delete()
    return redirect('manage-staffs')

@permission_required('is_staff')
def edit_customers(request, c_id):
    customer = User.objects.get(pk=c_id)

    form = UserUpdateForm(instance=customer)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('manage-customers')



    context ={'form':form, 'customer':customer}
    return render(request,'staff-pages/edit-customers.html', context)


### Edit/Update staffs
@permission_required('is_staff')
def edit_staffs(request, s_id):
    staff = User.objects.get(pk=s_id)

    form = UserUpdateForm(instance=staff)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('manage-staffs')



    context ={'form':form, 'staff':staff}
    return render(request,'staff-pages/edit-staffs.html', context)


@permission_required('is_admin')
def manage_orders(request):

    orders = Order.objects.filter(Q(o_placed=True) & ~Q(o_status="Completed")).order_by('-id')
    # for order in orders:
        
    #     shipping = order.shippingdetails_set.all()
        #print(shipping)
            
    #print(orders)
    
    
    context={'orders':orders}
    return render(request, 'staff-pages/orders.html', context)


@permission_required('is_staff')
def update_status(request, o_id):
    order = Order.objects.get(id=o_id)

    form = UpdateOrderForm

    if request.method == "POST":
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')


    context = {'order':order}
    return render(request, 'staff-pages/update-orders.html', context)