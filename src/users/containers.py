from injector import singleton

from src.users.repositories import UserCommandRepository
from src.users.repositories import UserQueryRepository
from src.users.services import UserLookupService
from src.users.stories import SignUpStory
from src.users.stories import UpdatePersonalInfoUserStory


def configure(binder):
    # repositories
    binder.bind(UserQueryRepository, to=UserQueryRepository, scope=singleton)
    binder.bind(UserCommandRepository, to=UserCommandRepository, scope=singleton)

    # stories
    binder.bind(UpdatePersonalInfoUserStory, to=UpdatePersonalInfoUserStory, scope=singleton)
    binder.bind(SignUpStory, to=SignUpStory, scope=singleton)

    # services
    binder.bind(UserLookupService, to=UserLookupService, scope=singleton)
