from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from os import name

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('account/', include('account.urls')),
    path('', include('base.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
