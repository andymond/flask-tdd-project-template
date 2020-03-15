from project import db

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
