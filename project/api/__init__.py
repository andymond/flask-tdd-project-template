from flask_restx import Api

from project import admin
from project.api.admin_users.views import LoginView, LogoutView
from project.api.ping import ping_namespace
from project.api.sample_items.views import sample_items_namespace

api = Api(version="1.0", title="myproject API", doc="/doc/")

admin.add_view(LoginView(name="Log In", url="login"))
admin.add_view(LogoutView(name="Log Out", url="logout"))

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(sample_items_namespace, path="/sample_items")
