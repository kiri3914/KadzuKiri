from django.shortcuts import render
from .models import StatusDeliver, Delivery
from .serializers import StatusDeliverSerializer, DeliverySerializer
from rest_framework import viewsets


class StatusDeliverViewSet(viewsets.ModelViewSet):
    queryset = StatusDeliver.objects.all()
    serializer_class = StatusDeliverSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer