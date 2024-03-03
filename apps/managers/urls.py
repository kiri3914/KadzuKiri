<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# write your routers here 

urlpatterns = router.urls
=======
"""
Register some views
# https://www.django-rest-framework.org/api-guide/routers/

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('category', views.CategoryViewSet)
router.register('news', views.NewsViewSet)

urlpatterns = router.urls
"""

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# write your routers here 

urlpatterns = router.urls
>>>>>>> e5d2cd847aaf3a7251e7a50cf99feea202f27fb1
