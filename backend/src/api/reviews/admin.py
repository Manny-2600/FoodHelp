from flask_admin.contrib.sqla import ModelView


class ReviewsAdminView(ModelView):
    column_searchable_list = ("restaurant_id", "user_id")
    column_editable_list = ("rating", "text")
    column_filters = ("restaurant_id",)
    column_sortable_list = ("restaurant_id", "user_id")
    column_default_sort = ("restaurant_id", True)
