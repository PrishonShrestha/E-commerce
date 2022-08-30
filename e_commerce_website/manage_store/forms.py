from django import forms
from .models import Category, Product

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['c_name', 'c_description', 'c_img'] 

class CreateProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['p_name', 'p_code', 'p_description', 'p_image', 'p_stock', 'p_price', 'p_category']
