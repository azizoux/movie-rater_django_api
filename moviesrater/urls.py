from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
