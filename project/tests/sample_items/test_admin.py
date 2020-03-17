import os
from project.api.admin_users.models import AdminUser
from project.services.db import base as db_service


def test_admin_view(test_app, test_database):
    admin = db_service.create(AdminUser, username="admin", email="admin@email.com", password="password", password_conf="password")
    @test_app.login_manager.request_loader
    def load_user_from_request(request):
        return admin
    client = test_app.test_client()
    admin_uri = os.environ.get("ADMIN_NAMESPACE")
    resp = client.get(admin_uri + "/sample_items/")
    assert resp.status_code == 200
