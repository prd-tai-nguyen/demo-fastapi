from fastapi import FastAPI

from controllers.user_controller import user_route
from controllers.auth_controller import auth_route

app = FastAPI()

app.include_router(router = user_route, prefix='/users')
app.include_router(router = auth_route, prefix='/auth')