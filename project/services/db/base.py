from project import db

def all(cls):
    return cls.query.all()

def find(cls, id):
    return cls.query.filter_by(id=id).first()
