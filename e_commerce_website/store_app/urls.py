from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('cart/', views.cartPage, name='cart'),
    path('shop/', views.shopPage, name='shop'),

    path('shop/<int:id>', views.filter_shop, name='filter-shop'),
    path('product-detail/<int:p_id>', views.product_detail, name='product-detail'),

]