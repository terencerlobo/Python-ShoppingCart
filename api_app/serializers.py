from dataclasses import field, fields
from email.policy import default
from pyexpat import model
from typing_extensions import Required
from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_quantity = serializers.IntegerField(required=False, default=1)
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()

    class Meta:
        model = CartItem
        fields = ('__all__')