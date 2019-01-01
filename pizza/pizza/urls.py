"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('detail/<str:name>', detail, name="detail"),
    path('order/<int:pizza_id>', order, name="order"),
    path('login', login, name='login'),
    path('logout', logoutme, name='logout'),
    path('registration', registration, name='registration')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
