from flask_restx import Api

from project.api.ping import ping_namespace
from project.api.sample_items.views import sample_items_namespace

api = Api(version="1.0", title="myproject API", doc="/doc/")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(sample_items_namespace, path="/sample_items")
