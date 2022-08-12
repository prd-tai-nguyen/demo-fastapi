from typing import List

from fastapi import Depends, Request, APIRouter

from schemas.user_schema import User
from repo.auth_repo import auth_repo
from repo.user_repo import user_repo

user_route = APIRouter()

@user_route.get("/{user_id}", response_model=User)
def find_user(user_id: int, user=Depends(auth_repo.validate_token)):
    users = user_repo.get_user(user_id=user_id)
    return users


@user_route.get("/", response_model=List[User])
def find_user(request: Request, user=Depends(auth_repo.validate_token)):
    return user_repo.get_users(**request.query_params)
