from flask import Flask, render_template
from flask_graphql import GraphQLView
from config import config
from database.db import db_init, db_session
from schema import schema
from datetime import datetime


app = Flask(__name__, 
    static_url_path='', 
    static_folder='resources/assets',
    template_folder='resources/views')
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.debug = config['DEBUG']


@app.template_filter()
def formatdate(value, format='%Y-%m-%dT%H:%M:%S'):
    date = datetime.strptime(value, format)
    return date.strftime('%B %d, %Y')


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.route('/', methods=['GET'])
def index():
    query = """{
      events {
        edges {
          node {
            title
            description
            occurredOn
          }
        }
      }
    }"""
    results = schema.execute(query)
    events = results.data['events']['edges']
    return render_template('index.html', events=events)


@app.route('/administrator/events/create', methods=['GET'])
def create_event():
    return render_template('events/create.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    db_init()
    app.jinja_env.filters['formatdate'] = formatdate
    app.run(port=5000)
