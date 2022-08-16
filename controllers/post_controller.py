from typing import List

from fastapi import Depends, Request, APIRouter, HTTPException, Header

from schemas import Post, PostCreate, PostResponse
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


@post_route.get("/")
def find(limit: int = 10, skip: int = 0, user=Depends(auth_repo.validate_token)):
  
    return post_repo.find(limit=limit, skip = skip, user_id=user.id)


@post_route.get("/{post_id}/comment", response_model=Post)
def find_comment(post_id: int, user=Depends(auth_repo.validate_token)):
    return post_repo.find_comment(user_id=user.id, post_id=post_id)


@post_route.post("/", response_model=Post)
def create(data: PostCreate, user=Depends(auth_repo.validate_token)):
    return post_repo.create(data=data, user_id=user.id)


@post_route.patch("/{post_id}")
def update(post_id: int, data: PostCreate, user=Depends(auth_repo.validate_token)):
    result = post_repo.update(
        data=data, post_id=post_id, user_id=user.id)
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
