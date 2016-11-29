# -*- coding:utf-8 -*-

from {{cookiecutter.app_name}}.app import app

def run_app(host='0.0.0.0', port=9090, debug=True):
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    run_app()