from django.urls import path
from . import views


urlpatterns = [

    ##### Manage Category
    path('managecategory/', views.manageCategoryPage, name='manage-category'),
    path('deletecategory/<int:c_id>', views.delete_category, name="delete-category"),
    path('managecategory/editcategory/<int:c_id>', views.edit_category, name="edit-category"),

    ##### Manage Products
    path('manageproducts/', views.manage_product, name='manage-products'),
    path('deleteproducts/<int:p_id>', views.delete_products, name="delete-products"),
    path('manageproducts/editproducts/<int:p_id>', views.edit_products, name='edit-products'),
]