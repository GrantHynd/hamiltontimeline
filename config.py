DATABASE_FILE = 'data.sqlite3'

config = {
    'DATABASE_FILE': DATABASE_FILE,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///database/' + DATABASE_FILE,
    'DEBUG': False,
    'PROPAGATE_EXCEPTIONS': True,
    'TEMPLATE_FOLDER': 'resources/views',
    'STATIC_URL_PATH': '',
    'STATIC_FOLDER': 'resources/assets'
}
