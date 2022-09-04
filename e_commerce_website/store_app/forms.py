from socket import fromshare
from .models import ShippingDetails, Order
from django import forms


class ShippingDetailsForm(forms.ModelForm):
    class Meta:
        model = ShippingDetails
        fields = ['order', 's_full_name', 's_email', 's_contact', 's_address']

class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['o_status', 'o_placed']