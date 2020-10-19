import graphene

import contas.schema
import usuarios.schema

class Query(usuarios.schema.Query, contas.schema.Query, graphene.ObjectType):
    pass

class Mutation(usuarios.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)