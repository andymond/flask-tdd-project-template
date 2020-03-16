from project.services.db import base as db_service


def test_admin_view(test_app, test_database):
    client = test_app.test_client()
    resp = client.get("/admin/sample_items/")
    assert resp.status_code == 200
