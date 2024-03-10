from django.shortcuts import render
from .models import Delivery
from .serializers import DeliverySerializer
from rest_framework import viewsets


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer