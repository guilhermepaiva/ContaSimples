import graphene
from graphene_django import DjangoObjectType

from .models import Conta

class ContaType(DjangoObjectType):
    class Meta:
        model = Conta

class Query(graphene.ObjectType):
    contas = graphene.List(ContaType)
    saldo_por_conta = graphene.Field(ContaType, numero=graphene.String(required=True))

    def resolve_contas(self, info, **kwargs):
        return Conta.objects.all()

    def resolve_saldo_por_conta(self, info, numero):
        try:
            return Conta.objects.get(numero=numero)
        except Conta.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)