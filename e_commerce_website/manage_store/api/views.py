from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .serializers import productSerializers

from manage_store.models import Product

from manage_store.api import serializers

##Details of all products
@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = productSerializers(products, many=True)
    return Response(serializer.data)


### Details of single product
@api_view(['GET'])
def productDetail(request, id):
    product_detail = Product.objects.get(id=id)
    serializer = productSerializers(product_detail, many=False)
    return Response(serializer.data)


## Add product
@api_view(['POST'])
def addProduct(request):
    serializer = productSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


### Update products
@api_view(['POST'])
def updateProduct(request, id):
    product = Product.objects.get(id=id)
    serializer = productSerializers(data=request.data, instance=product)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)