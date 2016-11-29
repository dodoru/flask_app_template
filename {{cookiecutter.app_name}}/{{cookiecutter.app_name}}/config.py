import os

env = os.environ.get

SQLALCHEMY_DATABASE_URI = env('SQLALCHEMY_DATABASE_URI', 'sqlite://')
SQLALCHEMY_TRACK_MODIFICATIONS = False


try:
    from .local_config import *
except ImportError:
    pass
