from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    path('confirm-email/<str:uidb64>/<str:token>/', views.ConfirmEmailView.as_view(), name='confirm-email'),

]

urlpatterns += router.urls