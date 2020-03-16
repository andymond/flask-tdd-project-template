import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3", url=os.environ.get("ADMIN_NAMESPACE") or "/admin/")


def create_app():
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)
    admin.init_app(app)

    from project.api import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
