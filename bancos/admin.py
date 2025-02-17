from django.contrib import admin
from .models import Banco, Movimentacao

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_conta', 'nome_gerente', 'contato_gerente')
    search_fields = ('nome', 'numero_conta', 'nome_gerente')

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('banco', 'data', 'documento', 'tipo', 'valor')
    list_filter = ('banco', 'tipo', 'data')
    search_fields = ('documento', 'descricao')
    date_hierarchy = 'data'
