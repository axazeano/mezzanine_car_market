__author__ = 'vladimir'
from rest_framework import serializers
from cartridge.shop.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product


class OrderSerialize(serializers.ModelSerializer):

    class Meta:
        model = Order


class DeliverySerializer(serializers.Serializer):
    product_description = serializers.CharField(max_length=1000)
    count = serializers.IntegerField()
    cost = serializers.FloatField()
    shop_name = serializers.CharField(max_length=200)