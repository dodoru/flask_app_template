import os

env = os.environ.get

SECRET_KEY = 'We come toward thee :-)'

SQLALCHEMY_DATABASE_URI = env('SQLALCHEMY_DATABASE_URI', 'sqlite:///{{cookiecutter.app_name}}_dev.bak.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from .local_config import *
except ImportError:
    pass
