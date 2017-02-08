import logging
from flask import Flask

from .models import db
from .utils import CustomJSONEncoder


def create_app(config=None):
    _app = Flask(__name__)
    _app.json_encoder = CustomJSONEncoder
    config_app(_app, config)
    init_app_logger(_app)
    init_app_blueprint(_app)
    return _app


def config_app(app, config=None, _default='src.config'):
    #: load default configuration
    app.config.from_object(_default)

    #: load app specified configuration
    if config and isinstance(config, dict):
        app.config.update(config)


def init_app_blueprint(app):
    ''' register new blueprint here '''
    from .views.error_handler import err_bp
    app.register_blueprint(err_bp)


def init_app_logger(app):
    # initialize logger
    logger = app.logger

    level = app.config.get('LOG_LEVEL', logging.DEBUG)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter(
        '[%(asctime)s]%(module)s - %(funcName)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logfile = app.config.get('LOG_FILE', None)
    if logfile is not None:
        fhdl = logging.FileHandler(filename=logfile)
        fhdl.setFormatter(formatter)
        logger.addHandler(fhdl)

    return logger


app = create_app()
db.init_app(app=app)
db.app = app
db.create_all()


@app.errorhandler(500)
def errorhandler_500(e):
    # 500 can not register on per_blueprint
    return 'server internal error'


@app.route('/ping')
def ping():
    return 'pong'
