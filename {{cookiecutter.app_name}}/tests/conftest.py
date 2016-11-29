import pytest

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.models import db


@pytest.fixture(autouse=True)
def core_app(tmpdir_factory):
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': 'sqlite://',
        'TESTING': True,
    })

    context = app.app_context()
    context.push()

    db.init_app(app)
    db.create_all()

    yield app

    db.session.rollback()
    context.pop()
