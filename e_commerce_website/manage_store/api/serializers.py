from rest_framework import serializers

from manage_store.models import Product

class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'p_name', 'p_code', 'p_description', 'p_image', 'p_stock', 'p_price', 'p_category']