from fastapi import FastAPI

from controllers.user_controller import user_route
from controllers.auth_controller import auth_route
from controllers.post_controller import post_route
from controllers.comment_controller import comment_route

app = FastAPI()

app.include_router(router = user_route, prefix='/users')
app.include_router(router = auth_route, prefix='/auth')
app.include_router(router = post_route, prefix='/posts')
app.include_router(router = comment_route, prefix='/comments')