# flask_app_template

A flask template for [cookiecutter](https://cookiecutter.readthedocs.io).

基本目录树和很接近这本书 <Flask Web开发：基于Python的Web应用开发实战>
https://book.douban.com/subject/26274202/

## Usage

```bash
$ pip install cookiecutter
$ cookiecutter https://github.com/dodoru/flask_app_template.git checkout={git_tag}
```

===

##### v0版树目录结构如下

    .
    ├── README.md
    ├── requirements.txt
    ├── deploy-requirements.txt
    ├── dev-requirements.txt
    ├── supervisord.conf
    ├── gunicorn_conf.py
    ├── manage.py
    ├── run.py
    ├── wsgi.py
    ├── scripts
    │   └── __init__.py
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   └── models
    │       └── __init__.py
    └── {{cookiecutter.app_name}}
        ├── __init__.py
        ├── app.py
        ├── config.py
        ├── errors.py
        ├── models
        │   └── __init__.py
        ├── templates
        │   └── error
        │       ├── 400.html
        │       ├── 401.html
        │       └── 404.html
        ├── utils.py
        └── views
            ├── __init__.py
            └── error_handler.py
    


