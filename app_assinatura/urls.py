from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assinaturas', views.listar_assinaturas, name='assinatura'),
]