from project import db

def all(cls):
    return cls.query.all()
