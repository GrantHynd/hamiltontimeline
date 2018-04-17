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
        try:
            event = EventModel(
                title=event_input.get('title'),
                description=event_input.get('description'),
                occurred_on=event_input.get('occurred_on')
            )
            event.save_to_db()
            return CreateEvent(event=event)
        except ValueError as error:
            return CreateEvent(error)


class UpdateEvent(relay.ClientIDMutation):
    class Input:
        id = graphene.Int(required=True)
        title = graphene.String(required=False)
        description = graphene.String(required=False)
        occurred_on = graphene.String(required=False)

    event = graphene.Field(Event)
    status = graphene.Field(graphene.String)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **event_input):
        status = None
        event = EventModel.find_by_id(event_input.get('id'))
        if event is not None:
            event.title = event_input.get('title')
            event.description = event_input.get('description')
            event.set_occurred_on(event_input.get('occurred_on'))
            event.save_to_db()
            status = "ok"
        else:
            status = "event with ID {} not found.".format(event_input.get('id'))
        return UpdateEvent(event=event, status=status)


class DeleteEvent(relay.ClientIDMutation):
    class Input:
        id = graphene.Int(required=True)

    status = graphene.Field(graphene.String)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **event_input):
        status = None
        event = EventModel.find_by_id(event_input.get('id'))
        if event is not None:
            event.delete_from_db()
            status = "ok"
        else:
            status = "event with ID {} not found.".format(event_input.get('id'))
        return DeleteEvent(status=status)
