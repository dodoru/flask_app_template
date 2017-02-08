# -*- coding:utf-8 -*-

import pytest

import json
from flask import Response

from src.app import create_app, app
from src.models import db


class APIResponse(Response):
    def get_json(self):
        return json.loads(self.data)


@pytest.fixture
def core_app(tmpdir_factory):
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///{{cookiecutter.app_name}}_test.bak.sqlite',
        'TESTING': True,
    })

    context = app.app_context()
    context.push()

    db.init_app(app)
    db.create_all()

    yield app

    db.session.rollback()
    context.pop()


@pytest.fixture(autouse=True)
def test_client():
    return app.test_client()


def test_ping_client(test_client, core_app):
    resp = test_client.get('/ping')
    assert resp.status_code == 200
    assert resp.data == 'pong'

    resp = core_app.test_client().get('/ping')
    assert resp.status_code == 404
