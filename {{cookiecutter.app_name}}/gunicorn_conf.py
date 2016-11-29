# RTFM -> http://docs.gunicorn.org/en/latest/settings.html#settings

bind = '0.0.0.0:9090'
workers = 7

timeout = 30

max_requests = 2000
max_requests_jitter = 500

proc_name = '{{cookiecutter.app_name}}'

accesslog = '-'
errorlog = '-'
loglevel = 'info'
