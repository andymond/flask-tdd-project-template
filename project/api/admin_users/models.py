from project import, login_manager

from sqlalchemy.sql import func
from passlib.apps import custom_app_context as pwd_context


class AdminUser(db.Model):
    __tablename__ = "admin_users"

    id = db.Column(db.BigInteger(), primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    authenticated = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    deleted_at = db.Column(db.DateTime, default=None)

    def __init__(self, **kwargs):
        self.username = kwargs["username"]
        self.email = kwargs["email"]
        if not kwargs["password"] == kwargs["password_conf"]:
            raise ValueError("Password Must Match Confirmation")
        self.password_hash = pwd_context.encrypt(kwargs["password"])

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return text_type(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
