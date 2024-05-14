from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assinaturas', views.listar_assinaturas, name='assinatura'),
    path('pagamento/<int:produto_id>/', views.pagamentoproduto1, name='pagamento'),

    path('compracerta', views.compracerta, name='compracerta'),
    path('compraerrada', views.compraerrada, name='compraerrada'),
]