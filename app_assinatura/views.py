from django.shortcuts import render
from .pagamento import pagamentoproduto1

from .models import Assinatura

def listar_assinaturas(request):
    assinaturas = Assinatura.objects.all()
    return render(request, 'assinaturas.html', {'assinaturas': assinaturas})

def home(request):
    return render(request, 'home.html')


def compracerta(request):
    return render(request,'compracerta.html')

def compraerrada(request):
    return render(request,'compraerrada.html')