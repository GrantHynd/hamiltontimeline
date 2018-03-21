import graphene
from schema.event import CreateEvent


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
