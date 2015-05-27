from cartridge.shop.models import Product
from rest_framework.serializers import ModelSerializer

__author__ = 'vladimir'

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product