from rest_framework import viewsets, views
from .serializers import CategoriaSerializer, EquipamentoSerializer, FuncionarioSerializer, MovimentacaoSerializer, UnidadeSerializer
from .models import Categoria, Equipamento, Funcionario, Movimentacao, Unidade
from .movimentacao_service import MovimentacaoService
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EquipamentoFilter


# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EquipamentoFilter

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # Passa os dados validados para o service criar a movimentação
        movimentacao = MovimentacaoService.criar_movimentacao(serializer.validated_data)
        serializer.instance = movimentacao

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    