import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay
from models.event import Event as EventModel


class Event(SQLAlchemyObjectType):
    class Meta:
        model = EventModel
        interfaces = (relay.Node, )


class CreateEvent(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        occurred_on = graphene.String(required=True)

    event = graphene.Field(Event)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **event_input):
        event = EventModel(
            title=event_input.get('title'),
            description=event_input.get('description'),
            occurred_on=event_input.get('occurred_on')
        )
        event.save_to_db()
        return CreateEvent(event=event)
