import json
from project.api.sample_items.models import SampleItem
from project.services.db import base as db_service
import pytest


def test_get_all_sample_items_valid(test_app, test_database):
    items = [
        db_service.create(SampleItem, name=name) for name in ["item1", "item2", "item3"]
    ]
    client = test_app.test_client()
    resp = client.get("/sample_items")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == len(items)
    assert data[0]["name"] == items[0].name
    assert data[1]["name"] == items[1].name
    assert data[2]["name"] == items[2].name


def test_get_single_sample_item_valid(test_app, test_database):
    item = db_service.create(SampleItem, name= "item1")
    client = test_app.test_client()
    resp = client.get(f"/sample_items/{item.id}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["name"] == item.name


def test_get_single_sample_item_invalid(test_app, test_database):
    item = db_service.create(SampleItem, name= "item1")
    client = test_app.test_client()
    resp = client.get(f"/sample_items/0")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404


def test_create_sample_item_valid(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/sample_items",
        data=json.dumps({ "name": "coolname" }),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "Resource created" in data["message"]


def test_create_sample_item_invalid(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/sample_items",
        data=json.dumps({"bad_key": "coolvalue"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_update_sample_item_valid(test_app, test_database):
    item = db_service.create(SampleItem, name="item1")
    client = test_app.test_client()
    resp = client.put(
        f"/sample_items/{item.id}",
        data=json.dumps({"name": "coolvalue"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "coolvalue" in data["name"]


@pytest.mark.parametrize(
    "item_id, payload, status_code, message",
    [
        [1, {}, 400, "Input payload validation failed"],
        [1, {"badkey": "updateditem"}, 400, "Input payload validation failed"],
        [
            999,
            {"name": "mrdoesntexist"},
            404,
            "Sample Item #999 not found",
        ],
    ],
)
def test_update_user_invalid(
    test_app, test_database, item_id, payload, status_code, message
):
    client = test_app.test_client()
    resp = client.put(
        f"/sample_items/{item_id}", data=json.dumps(payload), content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == status_code
    assert message in data["message"]


def test_delete_user_valid(test_app, test_database):
    item = db_service.create(SampleItem, name="item1")
    client = test_app.test_client()
    resp = client.delete(f"/sample_items/{item.id}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert f"Deleted Sample Item #{item.id}" in data["message"]


def test_delete_user_invalid(test_app, test_database):
    client = test_app.test_client()
    resp = client.delete(f"/sample_items/0")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert f"Sample Item #0 not found" in data["message"]
