from flask_admin.contrib.sqla import ModelView


class RestaurantsAdminView(ModelView):
    column_searchable_list = "name"
    column_editable_list = ("name",)
    column_filters = ("cuisines",)
    column_sortable_list = (
        "name",
        "cuisines",
    )
    column_default_sort = ("name", True)
