from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductImageViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')
router.register('product_pics', ProductImageViewSet, basename='product_pics')

urlpatterns = router.urls
