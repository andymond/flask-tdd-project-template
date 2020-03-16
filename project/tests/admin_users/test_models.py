from project.api.admin_users.models import AdminUser
from project.services.db import base as db_service
import pytest
from sqlalchemy.exc import IntegrityError


def test_valid_sample_item(test_app, test_database):
    attrs = {
        "username": "cooladmin",
        "email": "cool@admin.fake",
        "password": "Password123!",
        "password_conf": "Password123!"
    }
    admin = db_service.create(AdminUser, **attrs)
    assert admin.id == 1
    assert admin.username == "cooladmin"
    assert admin.verify_password("Password123!")

def test_password_must_match_conf(test_app, test_database):
    with pytest.raises(ValueError) as conf_err:
        attrs = {
            "username": "cooladmin",
            "email": "cool@admin.fake",
            "password": "Password123!",
            "password_conf": "wrong"
        }
        admin = db_service.create(AdminUser, **attrs)
    assert "Password Must Match Confirmation" in str(conf_err.value)
