import mercadopago
from .models import Assinatura
from django.http import HttpResponse
from django.shortcuts import redirect

def pagamentoproduto1(request,produto_id):
    produto = Assinatura.objects.get(id=produto_id)
    id_do_produto = produto.id
    nome_do_produto = produto.nome_assinatura
    descricao_do_produto = produto.descricao
    preco_do_produto = float(produto.preco)
    

    sdk = mercadopago.SDK("Access Token")

    payment_data = {
    "items": [
        {
            "id": 1,
            "title": nome_do_produto,
            "quantity": 1,
            "currency_id": "BRL",
            "unit_price": preco_do_produto,
        }
    ],
    "back_urls": {
        "success": "http://127.0.0.1:8000/compracerta",
        "failure": "http://127.0.0.1:8000/compraerrada",
        "pending": "http://127.0.0.1:8000/compraerrada",
    },
    "auto_return": "all",
    
}

    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return redirect(link_iniciar_pagamento)
