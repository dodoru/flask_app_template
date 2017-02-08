# -*- coding:utf-8 -*-

from flask import Blueprint, render_template
from src.errors import ConflictError, UnauthorizedError

err_bp = Blueprint('err_bp', __name__, template_folder='templates')


@err_bp.errorhandler(400)
@err_bp.errorhandler(ConflictError)
def badrequest(e):
    return render_template('error/400.html'), 400


@err_bp.errorhandler(401)
@err_bp.errorhandler(UnauthorizedError)
def resource_not_found(e):
    return render_template('error/401.html'), 409


@err_bp.errorhandler(404)
def resource_not_found(e):
    return render_template('error/404.html'), 404


