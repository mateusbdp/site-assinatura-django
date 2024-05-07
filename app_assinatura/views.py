from django.shortcuts import render

from .models import Assinatura

def listar_assinaturas(request):
    assinaturas = Assinatura.objects.all()
    return render(request, 'assinaturas.html', {'assinaturas': assinaturas})

def home(request):
    return render(request, 'home.html')