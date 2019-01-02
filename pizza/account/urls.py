from django.urls import path, include
from .views import login, logoutme, registration, alogin

urlpatterns = [
    path('alogin', alogin, name='alogin'),
    path('login', login, name='login'),
    path('logout', logoutme, name='logout'),
    path('registration', registration, name='registration')
]
