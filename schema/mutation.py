import graphene
from schema.event import CreateEvent, DeleteEvent


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    delete_event = DeleteEvent.Field()
