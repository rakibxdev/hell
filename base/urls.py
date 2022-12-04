from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('', views.home, name="Homepage"),
    path('login/', views.login, name="login"),
    path('signup/', views.sign, name="reg"),
]