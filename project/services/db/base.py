from project import db
from sqlalchemy import update

def all(cls):
    return cls.query.all()


def find(cls, id):
    return cls.query.filter_by(id=id).first()


def find_by(cls, **kwargs):
    return cls.query.filter_by(**kwargs).first()


def create(cls, **kwargs):
    record = cls(**kwargs)
    db.session.add(record)
    db.session.commit()
    return record


def update(record, **kwargs):
    for kw, v in kwargs.items():
        setattr(record, kw, v)
    db.session.commit()
    return record


def destroy(record):
    db.session.delete(record)
    db.session.commit()
    return record
