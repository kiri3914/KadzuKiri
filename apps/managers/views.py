from django.shortcuts import render
from .models import Department, Managers
from .serializers import DepartmentSerializer, ManagersSerializer
from rest_framework import viewsets


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ManagersViewSet(viewsets.ModelViewSet):
    queryset = Managers.objects.all()
    serializer_class = ManagersSerializer