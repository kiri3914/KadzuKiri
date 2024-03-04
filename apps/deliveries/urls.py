from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import DeliveryViewSet, StatusDeliverViewSet

router = DefaultRouter()
router.register(r'delivery', DeliveryViewSet, basename='delivery')
router.register(r'status_delivery', StatusDeliverViewSet, basename='status_delivery')




urlpatterns = router.urls
