from typing import List

from fastapi import Depends, APIRouter, HTTPException

from schemas import Comment, CommentCreate, CommentUpdate
from repo.auth_repo import auth_repo
from repo.comment_repo import comment_repo

comment_route = APIRouter()


@comment_route.get("/{comment_id}", response_model=Comment)
def find_by_id(comment_id: int, user=Depends(auth_repo.validate_token)):
    result = comment_repo.find_by_id(comment_id=comment_id, user_id=user.id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"COMMENT_NOT_FOUND",

        )
    return result


@comment_route.get("/", response_model=List[Comment])
def find(limit: int = 10, skip: int = 0, user=Depends(auth_repo.validate_token)):
    return comment_repo.find(limit=limit, skip=skip, user_id=user.id)


@comment_route.post("/", response_model=Comment)
def create(data: CommentCreate, user=Depends(auth_repo.validate_token)):
    comment = comment_repo.create(data=data, user_id=user.id)
    if comment is None:
        raise HTTPException(
            status_code=404,
            detail=f"POST_NOT_FOUND",
        )

    return comment


@comment_route.patch("/{comment_id}")
def update(comment_id: int, data: CommentUpdate, user=Depends(auth_repo.validate_token)):
    result = comment_repo.update(
        data=data, comment_id=comment_id, user_id=user.id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"POST_NOT_FOUND",
        )

    return result


@comment_route.delete("/{comment_id}")
def delete(comment_id: int, user=Depends(auth_repo.validate_token)):
    result = comment_repo.delete(comment_id=comment_id, user_id=user.id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"POST_NOT_FOUND",
        )

    return result
