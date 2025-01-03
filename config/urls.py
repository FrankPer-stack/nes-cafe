from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.directive.urls')),
    path('users/', include('apps.users.urls')),  # Agregar las URLs de users
]
