from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login", views.loginuser, name="login"),
    path("registro", views.registro, name="registro"),
    path("logalt", views.logalt, name="logalt"),


]