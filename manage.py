#! /usr/bin/env python

from thermos import app, db
from flask_script import Manager, prompt_bool

from thermos.models import User

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='Piotr', email='pis@test.com', password='test'))
    db.session.add(User(username='Test', email='test@com.pl', password='test'))
    db.session.commit()
    print 'Initialized Database'

@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to lose all your data'):
        db.drop_all()
        print 'Dropped Database'

if __name__ == '__main__':
    manager.run()
