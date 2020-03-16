from flask_admin.contrib.sqla import ModelView

class SampleItemsAdminView(ModelView):
    column_searchable_list = (
        "id",
        "name",
    )

    column_default_sort = ("id", True)
