import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from schema.event import Event


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    events = SQLAlchemyConnectionField(Event)
