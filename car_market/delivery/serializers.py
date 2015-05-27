__author__ = 'vladimir'

from rest_framework import serializers
from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ('provider', 'dealer_delivery_id', 'delivery_status', 'product', 'product_count', 'cost', 'date',)