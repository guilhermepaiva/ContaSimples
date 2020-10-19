import graphene

import conta.schema

class Query(conta.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)