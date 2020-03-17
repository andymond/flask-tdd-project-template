import os

from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3", url=os.environ.get("ADMIN_NAMESPACE") or "/admin/")
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        from project.api.admin_users.models import AdminUser
        from project.services.db import base as db_service
        db_service.find(AdminUser, id=user_id)

    admin.init_app(app)

    from project.api import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
