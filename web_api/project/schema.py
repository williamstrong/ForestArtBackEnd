import graphene

import image_api.schema

class Query(image_api.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
