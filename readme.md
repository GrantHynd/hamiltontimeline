# Hamilton Timeline

A web application to highlight the events of Alexander Hamilton's life.

## Getting Started
### Prerequisites

Python 3.6 is required with a virtual environment:

```
pip install virtualenv
virtualenv venv
```

### Installing

Make sure the code editor is using the venv library and not global python. [Activate the venv](https://virtualenv.pypa.io/en/stable/userguide/#usage):

```
venv\Scripts\activate
```

Install the requirements.txt on the venv python version:
```
pip install -r requirements.txt
```

And start-up the flask server:

```
python app.py
```

Interact with the GraphQL API via **http://127.0.0.1:5000/graphql**

## Running the tests

Run the automated tests for this system:
```
pip install pytest
python -m pytest tests/
```

## Built With

* [Flask](http://flask.pocoo.org/) - Microframework.
* [Graphene](http://graphene-python.org/) - Library for GraphQL APIs.
* [SQLAlchemy](http://www.sqlalchemy.org/) - SQL toolkit and ORM.
* [Pytest](https://docs.pytest.org/en/latest) - Testing framework.
* [Travis CI](https://travis-ci.org/) - Continuous integration testing tool.


## Authors

* **Grant Hynd** - (http://granthynd.co.uk)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Inspired by the life and work of Alexander Hamilton as communicated by Ron Chernow and Lin Manuel Miranda.
