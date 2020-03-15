from flask_restx import Resource, fields, Namespace

from project.api.sample_items.models import SampleItem
from project.services.db import base as db_service

sample_items_namespace = Namespace("sample_items")

sample_item_serializer = sample_items_namespace.model(
    "SampleItem",
    {
        "name": fields.String(required=True),
        "created_at": fields.String(required=True),
        "updated_at": fields.String,
    },
)


class SampleItems(Resource):
    @sample_items_namespace.marshal_with(sample_item_serializer, as_list=True)
    def get(self):
        return db_service.all(SampleItem)


sample_items_namespace.add_resource(SampleItems, "")
