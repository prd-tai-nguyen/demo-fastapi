from typing import List

from fastapi import Depends, Request, APIRouter

from schemas.user_schema import User
from schemas.post_schema import Post
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
def find(request: Request, user=Depends(auth_repo.validate_token)):
    return user_repo.find(**request.query_params)
