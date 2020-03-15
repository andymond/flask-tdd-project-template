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
        return db_service.all(SampleItem), 200

class SampleItemById(Resource):
    @sample_items_namespace.marshal_with(sample_item_serializer)
    def get(self, siid):
        sample_item = db_service.find(SampleItem, siid)
        if not sample_item:
            sample_items_namespace.abort(404, f"Sample Item #{siid} not found")
        return sample_item, 200


sample_items_namespace.add_resource(SampleItems, "")
sample_items_namespace.add_resource(SampleItemById, "/<int:siid>")
