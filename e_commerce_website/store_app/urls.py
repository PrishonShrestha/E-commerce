from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('cart/', views.cartPage, name='cart'),
    path('shop/', views.shopPage, name='shop'),

    path('shop/<int:id>', views.filter_shop, name='filter-shop'),
    path('product-detail/<int:p_id>', views.product_detail, name='product-detail'),

    path('checkout/ <int:o_id>', views.checkoutPage, name='checkout'),
    path('updateproducts/', views.updateProduct, name='update-products'),

    path('myorders/ <int:c_id>', views.myOrdersPage, name='my-orders'),

]