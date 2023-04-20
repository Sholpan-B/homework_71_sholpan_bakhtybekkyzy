"""instasram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import user_profile, follow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('user/', include('accounts.urls')),
    path('notifications/', include('notifications.urls')),
    path('<username>/', user_profile, name='profile'),
    path('<username>/saved', user_profile, name='profilefavorites'),
    path('<username>/follow/<option>', follow, name='follow'),
    path('api/', include('api.urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

