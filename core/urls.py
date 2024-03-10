
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import yasg

    # 'apps.authorization',
    # 'apps.customers',
    # "apps.deliveries",
    # "apps.managers",
    # "apps.products"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authorization.urls')),
    path('api/customers/', include('apps.customers.urls')),
    path('api/deliveries/', include('apps.deliveries.urls')),
    path('api/managers/', include('apps.managers.urls')),
    path('api/products/', include('apps.products.urls')),

]
urlpatterns += yasg.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

