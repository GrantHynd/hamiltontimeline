from flask import Flask
from flask_graphql import GraphQLView
from config import config
from database.db import engine, db_session, Base
from schema import schema


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.debug = config['DEBUG']

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            Base.metadata.create_all(bind=engine)

    app.run(port=5000)
