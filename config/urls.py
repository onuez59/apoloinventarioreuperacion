"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls import handler404
from core.pos.views.dashboard.views import page_not_found404
from rest_framework.authtoken import views


from django.views.generic import FormView, RedirectView

from core.login.views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('login/', include('core.login.urls')),
    path('pos/', include('core.pos.urls')),
    path('reports/', include('core.reports.urls')),
    path('user/', include('core.user.urls')),
    path('security/', include('core.security.urls')),
    path('api/', include('core.api.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]

# handler404 = page_not_found404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
