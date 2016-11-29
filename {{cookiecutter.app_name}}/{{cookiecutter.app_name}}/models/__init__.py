# -*- coding:utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class co_model():
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def remove(self):
        db.session.delete(self)
        db.session.commit()
        return self
