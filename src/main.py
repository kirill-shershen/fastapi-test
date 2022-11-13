from fastapi import FastAPI
from fastapi_injector import attach_injector
from sqladmin import Admin

from src.auth.views import auth_router
from src.config.settings import settings
from src.db.base import database
from src.db.base import engine
from src.db.base import metadata
from src.injection import di
from src.users.admin import UserAdmin
from src.users.views import users_router

app = FastAPI(title="Rialto", version="0.1.0", debug=settings.debug)


admin = Admin(app, engine)
admin.add_view(UserAdmin)
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
attach_injector(app, injector=di)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
