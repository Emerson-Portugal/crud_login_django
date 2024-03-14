# core/urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.login.urls', namespace='login')),
    path('accounts/', include('django.contrib.auth.urls')),
    
]