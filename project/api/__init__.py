from flask_restx import Api

from project.api.ping import ping_namespace

api = Api(version="1.0", title="myproject API", doc="/doc/")

api.add_namespace(ping_namespace, path="/ping")
