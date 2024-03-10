from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('client', views.ClientViewSet)
router.register('adress', views.AdressViewSet)
router.register('favorites', views.FavoritesViewSet)
router.register('cart', views.CartViewSet)
router.register('cartitem', views.CartItemViewSet)

urlpatterns = router.urls

