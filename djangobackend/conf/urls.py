"""djangobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth import views as auth_views

from baseapi.path import ReactPath

from . import views


urlpatterns = [
    ReactPath('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(
        'accounts/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset'
    ),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path(r'api-auth/', include('rest_framework.urls')),
    ] + urlpatterns
