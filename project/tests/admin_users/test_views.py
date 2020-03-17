import os
import flask_login
from project.api.admin_users.models import AdminUser
from project.services.db import base as db_service

login_url = os.environ.get("ADMIN_NAMESPACE") + "/login/"

def test_login_landing(test_app, test_database):
    client = test_app.test_client()
    resp = client.get(login_url)
    assert resp.status_code == 200

def test_login_valid(test_app, test_database):
    admin = db_service.create(AdminUser, username="cooladmin", email="cool@admin.fake", password="password", password_conf="password")
    client = test_app.test_client()
    resp = client.post(
        login_url,
        data={"username": admin.username, "password": "password"},
        content_type="multipart/form-data",
        follow_redirects=True
    )
    assert flask_login.utils.current_user.is_authenticated
    assert resp.status_code == 200
    assert "Logged in" in str(resp.data)
