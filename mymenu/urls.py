"""mymenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
import index

from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('accounts/register/',
        RegistrationView.as_view(success_url='/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace='index')),
    path('nutrinfo/', include('nutritionalinfo.urls', namespace='nutritionalinfo')),
    path('products/', include('products.urls', namespace='products')),
]

handler404 = index.views.handler404
handler500 = index.views.handler500