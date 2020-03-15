from project import db
from project.services.db import base
import pytest

from sqlalchemy import func


class Dummy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

def seed_dummies():
    names = ['dummy1', 'dummy2', 'dummy3']
    for name in names:
        dummy = Dummy(name=name)
        db.session.add(dummy)
    db.session.commit()

def test_all(test_app, test_database):
    seed_dummies()
    pass


def test_find(test_app, test_database):
    seed_dummies()
    pass


def test_find_by(test_app, test_database):
    pass


def test_create(test_app, test_database):
    pass


def test_destroy(test_app, test_database):
    pass
