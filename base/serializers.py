from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Order
#         fields='__all__'
