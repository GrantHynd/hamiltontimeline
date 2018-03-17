DATABASE_FILE = 'data.sqlite3'

config = {
    'DATABASE_FILE': DATABASE_FILE,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///database/' + DATABASE_FILE,
    'DEBUG': False,
    'PROPAGATE_EXCEPTIONS': True
}
