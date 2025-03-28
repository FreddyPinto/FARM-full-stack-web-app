from bson import ObjectId
from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from app.authentication import AuthHandler
from app.models.user_model import CurrentUserModel, LoginModel, UserModel

users_router = APIRouter()
auth_handler = AuthHandler()

@users_router.post("/register", response_description="Register user")
async def register(request: Request, newUser: LoginModel = Body(...)) -> UserModel:
    
    users = request.app.db["users"]
    # has the password before inserting it into MongoDB
    newUser.password = auth_handler.get_password_hash(newUser.password)
    newUser = newUser.model_dump()
    # check existing user or email 409 conflict
    if (
        existing_username := await users.find_one({"username": newUser["username"]})
        is not None
    ):
        raise HTTPException(
            status_code=409,
            detail=f"User with username {newUser['username']} already exists",
        )
    new_user = await users.insert_one(newUser)
    created_user = await users.find_one({"_id": new_user.inserted_id})

    return created_user
