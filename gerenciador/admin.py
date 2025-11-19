from django.contrib import admin
from .models import Unidade, Categoria, Funcionario, Equipamento, Movimentacao

# ---------- Admin Unidade ----------
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'endereco', 'n_cnes']
    search_fields = ['nome', 'endereco', 'n_cnes']
    ordering = ['nome']

# ---------- Admin Categoria ----------
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    ordering = ['nome']

# ---------- Admin Funcionario ----------
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cpf', 'unidade']
    search_fields = ['nome', 'cpf']
    list_filter = ['unidade']
    ordering = ['nome']

# ---------- Admin Equipamento ----------
@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nome', 'numero_patrimonio', 'categoria',
        'status', 'funcionario', 'qtde_estoque'
    ]
    search_fields = ['nome', 'numero_patrimonio']
    list_filter = ['status', 'categoria']
    ordering = ['nome']

# ---------- Admin Movimentacao ----------
@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'data',
        'equipamento',
        'origem_funcionario',
        'origem_unidade',   # método abaixo
        'destino_funcionario',
        'destino_unidade',  # método abaixo
    ]
    readonly_fields = ['data', 'origem_unidade', 'destino_unidade']
    list_filter = ['data', 'equipamento']
    search_fields = [
        'equipamento__nome',
        'origem_funcionario__nome',
        'destino_funcionario__nome'
    ]
    ordering = ['-data']

    # ---------- Métodos para exibir unidades ----------
    def origem_unidade(self, obj):
        if obj.origem_funcionario and obj.origem_funcionario.unidade:
            return obj.origem_funcionario.unidade.nome
        return '-'
    origem_unidade.short_description = 'Unidade de Origem'

    def destino_unidade(self, obj):
        if obj.destino_funcionario and obj.destino_funcionario.unidade:
            return obj.destino_funcionario.unidade.nome
        return '-'
    destino_unidade.short_description = 'Unidade de Destino'
