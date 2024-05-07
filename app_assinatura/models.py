from django.db import models
from django.contrib.auth.models import User

class Assinatura(models.Model):
    nome_assinatura = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_meses = models.PositiveIntegerField()

    def __str__(self):
        return self.nome_assinatura

class Pedido(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    assinatura = models.ForeignKey(Assinatura, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.username}"

class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=100)
    status_pagamento = models.CharField(max_length=100)

    def __str__(self):
        return f"Pagamento do Pedido {self.pedido_id}"
