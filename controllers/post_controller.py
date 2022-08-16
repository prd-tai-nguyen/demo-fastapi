from typing import List

from fastapi import Depends, Request, APIRouter, HTTPException

from schemas.post_schema import Post, PostCreate
from repo.auth_repo import auth_repo
from repo.post_repo import post_repo

post_route = APIRouter()


@post_route.get("/{post_id}", response_model=Post)
def find_by_id(post_id: int, user=Depends(auth_repo.validate_token)):
    result = post_repo.find_by_id(post_id=post_id, user_id=user.id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"POST_NOT_FOUND",

        )
    return result


@post_route.get("/", response_model=List[Post])
def find(request: Request, user=Depends(auth_repo.validate_token)):
    return post_repo.find(user_id=user.id, **request.query_params)


@post_route.post("/", response_model=Post)
def create(post_data: PostCreate, user=Depends(auth_repo.validate_token)):
    return post_repo.create(post_data=post_data, user_id=user.id)


@post_route.patch("/{post_id}")
def update(post_id: int, post_data: PostCreate, user=Depends(auth_repo.validate_token)):
    result = post_repo.update(
        post_data=post_data, post_id=post_id, user_id=user.id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"POST_NOT_FOUND",
        )

    return result


@post_route.delete("/{post_id}")
def delete(post_id: int, user=Depends(auth_repo.validate_token)):
    result = post_repo.delete(post_id=post_id, user_id=user.id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"POST_NOT_FOUND",
        )

    return result
