from typing import List

from fastapi import Depends, Request, APIRouter, HTTPException

from schemas import User, UserResponse
from repo.auth_repo import auth_repo
from repo.user_repo import user_repo

user_route = APIRouter()


@user_route.get("/post", response_model=User)
def find_post(request: Request, user=Depends(auth_repo.validate_token)):
    return user_repo.find_post(user_id=user.id, **request.query_params)


@user_route.get("/{user_id}", response_model=User)
def find_by_id(user_id: int, user=Depends(auth_repo.validate_token)):
    result = user_repo.find_by_id(user_id=user_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"USER_NOT_FOUND",

        )

    return result


@user_route.get("/", response_model=List[User])
def find(limit: int = 10, skip: int = 0, request: Request = None, user=Depends(auth_repo.validate_token)):
    return user_repo.find(limit=limit, skip=skip, **request.query_params)
