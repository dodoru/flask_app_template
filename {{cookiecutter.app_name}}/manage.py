from flask_script import Manager, Shell
from flask_script.commands import Clean, ShowUrls

from src.app import app, db

manager = Manager(app)

def _make_context():
    return dict(db=db)

@manager.command
def create_db():
    db.init_app(app=app)
    db.create_all()

@manager.command
def drop_db():
    db.init_app(app=app)
    db.drop_all()

manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('clean', Clean())
manager.add_command('show_urls', ShowUrls())

if __name__ == '__main__':
    manager.run()
