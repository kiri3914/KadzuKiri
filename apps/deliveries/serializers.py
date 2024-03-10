from rest_framework import serializers
from .models import Delivery, StatusDeliver


class StatusDeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDeliver
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'