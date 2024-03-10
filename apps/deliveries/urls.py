from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import DeliveryViewSet

router = DefaultRouter()
router.register(r'delivery', DeliveryViewSet, basename='delivery')




urlpatterns = router.urls
