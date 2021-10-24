from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Review,Order,OrderItem,ShippingAddress
from .products import products
from .serializers import ProductSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
    {
     '_id':'1',
     'name':'Tomato',
     'image':'https://www.pexels.com/photo/tomato-lot-1327838/',
     'price':120,
     'countinstock': 10,
    }
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    product=Product.objects.get(_id=pk)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)


# @api_view(['GET'])
# def getOrders(request):
#     orders=Order.objects.all()
#     serializer=ProductSerializer(orders,many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def getOrder(request,pk):
#     orders=Order.objects.get(_id=pk)
#     serializer=ProductSerializer(orders,many=False)
#     return Response(serializer.data)
