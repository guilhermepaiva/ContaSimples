from django.db.models import Q

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from usuarios.schema import UserType


from .models import Conta, Transacao

class ContaType(DjangoObjectType):
    class Meta:
        model = Conta

class TransacaoType(DjangoObjectType):
    class Meta:
        model = Transacao

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
    def resolve_transacao(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Transacao.objects.get(pk=id)

    def resolve_transacoes(self, info, **kwargs):
        return Transacao.objects.all()

class CreateConta(graphene.Mutation):
    id = graphene.Int()
    titular = graphene.String()
    numero = graphene.String()
    saldo = graphene.Float()

    class Arguments:
        titular = graphene.String()
        numero = graphene.String()

    def mutate(self, info, titular, numero):
        user = info.context.user
        conta = Conta(
            titular=titular,
            numero=numero,
        )
        conta.save()

        return CreateConta(
            id=conta.id,
            titular=conta.titular,
            numero=conta.numero,
        )

class CreateTransacao(graphene.Mutation):
    data = graphene.String()
    tipo = graphene.String()
    valor = graphene.Float()

    class Arguments:
        data = graphene.String()
        tipo = graphene.String()
        valor = graphene.Float()

    def mutate(self, info, data, tipo, valor):

        transacao = Transacao(
            data=data,
            tipo=tipo,
            valor=valor,
        )

        return CreateTransacao(
            data=data,
            tipo=tipo,
            valor=valor,
        )


#schema = graphene.Schema(query=Query)
class Mutation(graphene.ObjectType):
    create_conta = CreateConta.Field()
    create_transacao = CreateTransacao.Field()