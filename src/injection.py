from injector import Injector

from src.auth.containers import configure as auth_configure
from src.users.containers import configure as user_configure

di = Injector()
di.binder.install(auth_configure)
di.binder.install(user_configure)
