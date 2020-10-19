import graphene
from graphene_django import DjangoObjectType

from .models import Conta

class ContaType(DjangoObjectType):
    class Meta:
        model = Conta

class Query(graphene.ObjectType):
    contas = graphene.List(ContaType)

    def resolve_contas(self, info, **kwargs):
        return Conta.objects.all()