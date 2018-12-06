import os

SECRET_KEY = 'thisisthetestingsecretkey'
ARIA2_POST = 6800
FLV_POST = 6900


class Config(object):
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'scp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
