"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls.static import static

api_routers = [
    path('v1/', include('api_v1.urls')),
    path('v2/', include('api_v2.urls')),
    path('v3/', include('api_v3.urls')),
]

urlpatterns = [
    path('api/', include(api_routers)),
    path('i18n/', include('django.conf.urls.i18n')),
]

# localhost:8000/ru/articles
# localhost:8000/en/articles

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include("webapp.urls")),
    path('accounts/', include("accounts.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
