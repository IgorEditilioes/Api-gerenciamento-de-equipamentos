from django.db import models
from django.core.exceptions import ValidationError


class Unidade(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=300)
    n_cnes = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.SET_NULL,
        related_name='funcionarios',
        null=True
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Equipamento(models.Model):

    STATUS_CHOICES = (
        ('funcionando', 'Funcionando'),
        ('quebrado', 'Quebrado'),
        ('em manutencao', 'Em Manutenção'),
        ('roubado', 'Roubado'),
        ('em estoque', 'Em estoque'),
        ('fora de estoque', 'Fora de Estoque'),
    )

    nome = models.CharField(max_length=150)
    numero_patrimonio = models.PositiveIntegerField(
        blank=True,
        null=True,
        unique=True
    )
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=25)

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.SET_NULL,
        related_name='equipamentos',
        null=True
    )

    qtde_estoque = models.PositiveIntegerField(default=0)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    equipamento = models.ForeignKey("Equipamento", on_delete=models.CASCADE)
    origem_funcionario = models.ForeignKey(
        "Funcionario", related_name="origem", on_delete=models.CASCADE
    )
    destino_funcionario = models.ForeignKey(
        "Funcionario", related_name="destino", on_delete=models.CASCADE
    )

    def clean(self):
        if self.origem_funcionario == self.destino_funcionario:
            raise ValidationError("Funcionário de origem e destino devem ser diferentes.")