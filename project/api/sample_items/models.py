from project import db
from sqlalchemy.sql import func


class SampleItem(db.Model):
    __tablename__ = "sample_items"

    id = db.Column(db.BigInteger(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    deleted_at = db.Column(db.DateTime, default=None)
