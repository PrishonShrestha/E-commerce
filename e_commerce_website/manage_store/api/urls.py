from django.urls import path
from . import views

urlpatterns = [
    path('productlist/', views.productList, name='product-list'),
    path('product_detail/<int:id>', views.productDetail, name='product_detail'),
    path('addproduct/', views.addProduct, name='add-product'),
    path('update_product/<int:id>', views.updateProduct, name='update_product'),
]
