from project.api.sample_items.models import SampleItem
from project.services.db import base as db_service
import pytest
from sqlalchemy.exc import IntegrityError


def test_valid_sample_item(test_app, test_database):
    item = db_service.create(SampleItem, name="new item")
    assert item.id == 1
    assert item.name == "new item"


def test_name_required(test_app, test_database):
    with pytest.raises(IntegrityError):
        db_service.create(SampleItem, name=None)
