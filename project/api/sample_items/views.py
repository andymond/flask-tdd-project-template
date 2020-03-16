from flask import request
from flask_restx import Resource, fields, Namespace

from project.api.sample_items.models import SampleItem
from project.services.db import base as db_service

sample_items_namespace = Namespace("sample_items")

sample_item = sample_items_namespace.model(
    "SampleItem",
    {
        "name": fields.String(required=True),
        "created_at": fields.String,
        "updated_at": fields.String,
    },
)


class SampleItems(Resource):
    @sample_items_namespace.marshal_with(sample_item, as_list=True)
    def get(self):
        return db_service.all(SampleItem), 200

    @sample_items_namespace.expect(sample_item, validate=True)
    def post(self):
        post_data = request.get_json()
        db_service.create(SampleItem, **post_data)
        return {"message": "Resource created"}, 201


class SampleItemById(Resource):
    @sample_items_namespace.marshal_with(sample_item)
    def get(self, siid):
        sample_item = db_service.find(SampleItem, siid)
        if not sample_item:
            sample_items_namespace.abort(404, f"Sample Item #{siid} not found")
        return sample_item, 200

    @sample_items_namespace.expect(sample_item, validate=True)
    @sample_items_namespace.marshal_with(sample_item)
    def put(self, siid):
        sample_item = db_service.find(SampleItem, siid)
        if not sample_item:
            sample_items_namespace.abort(404, f"Sample Item #{siid} not found")
        put_data = request.get_json()
        updated_item = db_service.update(SampleItem, **put_data)
        return updated_item

    def delete(self, siid):
        sample_item = db_service.find(SampleItem, siid)
        if not sample_item:
            sample_items_namespace.abort(404, f"Sample Item #{siid} not found")
        db_service.destroy(sample_item)
        return {"message": f"Deleted Sample Item #{siid}"}


sample_items_namespace.add_resource(SampleItems, "")
sample_items_namespace.add_resource(SampleItemById, "/<int:siid>")
