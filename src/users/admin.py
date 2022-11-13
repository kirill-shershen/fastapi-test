from sqladmin import ModelView

from src.users.models import User


class UserAdmin(ModelView, model=User):  # type: ignore
    column_list = [User.id, User.name, User.surname, User.email, User.is_stuff]
    column_details_list = [User.id, User.name, User.surname, User.email, User.is_stuff]
    column_searchable_list = [User.name]
    column_default_sort = [(User.id, True)]
    page_size = 25
    page_size_options = [25, 50, 100, 200]
