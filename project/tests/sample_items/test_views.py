import json
from project.api.sample_items.models import SampleItem
from project.services.db import base as db_service


def test_get_all_sample_items(test_app, test_database):
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

def test_get_single_sample_item(test_app, test_database):
    item = db_service.create(SampleItem, name= "item1")
    client = test_app.test_client()
    resp = client.get(f"/sample_items/{item.id}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["name"] == item.name

    resp = client.get(f"/sample_items/0")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
