from project import db
from project.services.db import base as db_service
import pytest

from sqlalchemy import func


class Dummy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


def seed_dummies():
    names = ["dummy1", "dummy2", "dummy3"]
    for name in names:
        dummy = Dummy(name=name)
        db.session.add(dummy)
    db.session.commit()

def test_all(test_app, test_database):
    seed_dummies()
    dummies = db_service.all(Dummy)
    assert len(dummies) == 3


def test_find(test_app, test_database):
    seed_dummies()
    dummy1, dummy2, dummy3 = [db_service.find(Dummy, id) for id in [1, 2, 3]]
    assert dummy1.id == 1
    assert dummy1.name == "dummy1"
    assert dummy2.id == 2
    assert dummy2.name == "dummy2"
    assert dummy3.id == 3
    assert dummy3.name == "dummy3"


def test_find_by(test_app, test_database):
    seed_dummies()
    dummy1 = db_service.find_by(Dummy, id=1)
    dummy2 = db_service.find_by(Dummy, name="dummy2")
    assert dummy1.id == 1
    assert dummy1.name == "dummy1"
    assert dummy2.id == 2
    assert dummy2.name == "dummy2"


def test_create(test_app, test_database):
    pass


def test_destroy(test_app, test_database):
    pass
