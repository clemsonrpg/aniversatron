from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


# Routers provide an easy way of automatically determining the URL conf.


urlpatterns = [
    path('', include("apps.core.urls", namespace='core')),
    path('pessoas/', include('apps.pessoas.urls', namespace='pessoas')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)