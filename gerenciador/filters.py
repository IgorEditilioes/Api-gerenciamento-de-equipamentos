import django_filters
from .models import Equipamento

class EquipamentoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter(lookup_expr="iexact")
    data_registro_de = django_filters.DateFilter(field_name="data_registro", lookup_expr="gte")
    data_registro_ate = django_filters.DateFilter(field_name="data_registro", lookup_expr="lte")
    funcionario = django_filters.CharFilter(
        field_name='funcionario__nome',
        lookup_expr='icontains'
    )

    # Filtrar por nome da categoria
    categoria = django_filters.CharFilter(
        field_name='categoria__nome',
        lookup_expr='icontains'
    )

    class Meta:
        model = Equipamento
        fields = ["nome", "categoria", "status", "data_registro_de", "data_registro_ate"]
