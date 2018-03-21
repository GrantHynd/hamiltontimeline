import graphene
from schema.event import CreateEvent, UpdateEvent, DeleteEvent


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    delete_event = DeleteEvent.Field()
