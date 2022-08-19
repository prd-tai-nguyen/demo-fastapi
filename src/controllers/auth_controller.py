from fastapi import Depends, HTTPException, APIRouter
from schemas import UserCreate, User, UserLogin
from repo.auth_repo import auth_repo

auth_route = APIRouter()

@auth_route.post("/login/", tags=["auth"])
def login(user: UserLogin):
    access_token = auth_repo.login(email=user.email, password=user.password)
    if access_token is None:
        raise HTTPException(status_code=401, detail="Invalid login")
    return {"access_token": access_token}


@auth_route.post("/register/", tags=["auth"])
def register(user: UserCreate):
    access_token = auth_repo.register(user=user)
    if access_token is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"access_token": access_token}

@auth_route.get("/me/", response_model=User, tags=["auth"])
def get_current_user(user=Depends(auth_repo.validate_token)):
    return user