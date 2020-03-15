from project.api.sample_items.models import SampleItem
from project.services.db import base as db_service

def test_valid_sample_item(test_app, test_database):
    item = db_service.create(SampleItem, name="new item")
    assert item.id == 1
    assert item.name == "new item"
