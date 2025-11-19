from rest_framework import serializers
from .models import Categoria, Equipamento, Funcionario, Movimentacao, Unidade

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        exclude = []

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        exclude = []

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        exclude = []

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        exclude = []

        def validate(self, data):
        # Exemplo de regra de negócio simples no serializer
            if data['origem_funcionario'] == data['destino_funcionario']:
                raise serializers.ValidationError(
                    "O funcionário de origem e destino não podem ser iguais."
                )
            return data

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        exclude = []
