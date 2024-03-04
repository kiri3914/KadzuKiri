from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('manager', views.ManagersViewSet)
router.register('departament', views.DepartmentViewSet)

urlpatterns = router.urls