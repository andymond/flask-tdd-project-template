import os

from flask import redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class SampleItemsAdminView(ModelView):
    column_searchable_list = (
        "id",
        "name",
    )

    column_default_sort = ("id", True)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        login_url = os.environ.get("ADMIN_NAMESPACE") + "/login/"
        return redirect(login_url)
