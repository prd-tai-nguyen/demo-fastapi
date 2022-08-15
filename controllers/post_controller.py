from typing import List

from fastapi import Depends, Request, APIRouter

from schemas.post_schema import Post, PostCreate
from repo.auth_repo import auth_repo
from repo.post_repo import post_repo

post_route = APIRouter()

@post_route.get("/{post_id}", response_model=Post)
def find_post(post_id: int, user=Depends(auth_repo.validate_token)):
    users = post_repo.get_post(post_id=post_id)
    return users


@post_route.get("/", response_model=List[Post])
def find_posts(request: Request, user=Depends(auth_repo.validate_token)):
    return post_repo.get_posts(**request.query_params)


@post_route.post("/", response_model=Post)
def create_post(post_data: PostCreate, user=Depends(auth_repo.validate_token)):
    post = post_repo.create_post(post_data = post_data, user_id = user.id)
    return post
