
FROM daocloud.io/python:2.7.12-wheezy

MAINTAINER {{cookiecutter.maintainer}} <{{cookiecutter.maintainer_email}}>

RUN mkdir -p /data/{{cookiecutter.app_name}}
RUN mkdir -p /data/{{cookiecutter.app_name}}/log

WORKDIR /data/{{cookiecutter.app_name}}
COPY requirements.txt /data/{{cookiecutter.app_name}}/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

COPY . /data/{{cookiecutter.app_name}}/

## naive gunicorn
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:9300", "--worker-class", "gevent", "wsgi:app"]

## gunicorn with configuration
# CMD ["gunicorn", "-k", "gevent", "-c", "gunicorn_conf.py", "wsgi:app"]

## entry by superviord
# ENTRYPOINT ["supervisord", "-n"]
# CMD ["-c", "supervisord.conf"]