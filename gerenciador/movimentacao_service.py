
from .models import Movimentacao

class MovimentacaoService:

    @staticmethod
    def criar_movimentacao(data):
        equipamento = data["equipamento"]
        destino_funcionario = data["destino_funcionario"]

        # Atualiza o funcionário responsável pelo equipamento
        equipamento.funcionario = destino_funcionario
        equipamento.save()

        # Cria a movimentação no banco
        movimentacao = Movimentacao.objects.create(**data)

        return movimentacao