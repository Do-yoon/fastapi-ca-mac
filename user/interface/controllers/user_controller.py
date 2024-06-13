from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from user.application.user_service import UserService
from dependency_injector.wiring import inject, Provide
from containers import Container


router = APIRouter(prefix="/users")

class User(BaseModel):
    name: str
    email: str
    password: str

@router.post("")
@inject
def create_user(
    user: User,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    user_service = UserService()
    created_user = user_service.create_user(
        name=user.name,
        email=user.email,
        password=user.password
    )
 
    return created_user

class UpdateUser(BaseModel):
    name: str | None = None
    password: str | None = None
 
@router.put("/{user_id}")
@inject
def update_user(
    user_id: str,
    user: UpdateUser,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    user = user_service.update_user(
        user_id=user_id,
        name=user.name,
        password=user.password,
    )
 
    return user
