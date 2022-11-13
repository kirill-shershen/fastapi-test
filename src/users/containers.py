# from dependency_injector import containers, providers
from injector import singleton

from src.users.repositories import UserCommandRepository
from src.users.repositories import UserQueryRepository
from src.users.stories import UpdatePersonalInfoUserStory

# from src.db.containers import DB


def configure(binder):
    # repositories
    binder.bind(UserQueryRepository, to=UserQueryRepository, scope=singleton)
    binder.bind(UserCommandRepository, to=UserCommandRepository, scope=singleton)

    # stories
    binder.bind(UpdatePersonalInfoUserStory, to=UpdatePersonalInfoUserStory, scope=singleton)


# class UserRepository(containers.DeclarativeContainer):
#     user_query_repository = providers.Factory(UserQueryRepository, database=DB.database)
#     user_command_repository = providers.Factory(UserCommandRepository, database=DB.database)
#
#     get_current_user = providers.Factory(get_current_user, user_query=user_query_repository)
#
#
# class UserStory(containers.DeclarativeContainer):
#
#     update_personal_user_story = providers.Factory(
#         UpdatePersonalUserStory,
#         user_query=UserRepository.user_query_repository,
#         user_command=UserRepository.user_command_repository,
#         current_user=UserRepository.get_current_user
#     )
