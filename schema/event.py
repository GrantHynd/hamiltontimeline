from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay
from models.event import Event as EventModel


class Event(SQLAlchemyObjectType):
    class Meta:
        model = EventModel
        interfaces = (relay.Node, )
