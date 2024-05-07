from django.contrib import admin

from .models import Assinatura, Pedido, Pagamento

@admin.register(Assinatura)
class AssinaturaAdmin(admin.ModelAdmin):
    list_display = ('nome_assinatura', 'preco', 'duracao_meses','imagem')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data', 'assinatura')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'valor_total', 'data_pagamento', 'forma_pagamento', 'status_pagamento')
    list_filter = ('forma_pagamento', 'status_pagamento')
    search_fields = ['pedido__id', 'forma_pagamento', 'status_pagamento']