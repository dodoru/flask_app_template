# -*- coding:utf-8 -*-
import pytest

from src.app import app


def test_ping(test_client):
    resp = test_client.get('/ping')
    assert resp.status_code == 200
    assert resp.data == 'pong'


def test_api_on_method_get_without_args(test_client):
    rules = app.url_map._rules
    for rule in rules:
        url = rule.rule
        endpoint = rule.endpoint
        args = list(rule.arguments)
        methods = list(rule.methods)
        if 'GET' in methods and not bool(args):
            resp = test_client.get(url)
            status_code = resp.status_code
            data = resp.data
            # file_logger(endpoint, methods, data=data, result=status_code, stdout=True)
            print(endpoint, url, methods, status_code, data)
            assert status_code == 200
        else:
            print(endpoint, url, methods, args, 'xxx')
            # file_logger(endpoint, url, methods, args, result='jump with args', stdout=True)
