from apis.internal import admin_paths
from apis.version1 import card_paths
from apis.version1 import token_paths
from apis.version1 import user_paths
from db.repository.users import get_current_active_user
from fastapi import Depends
from fastapi import APIRouter


api_router = APIRouter()


api_router.include_router(
    card_paths.router,
    prefix = "/v1",
    tags = ["Cards"],
    dependencies= [Depends(get_current_active_user)]
)

api_router.include_router(
    user_paths.router,
    prefix = "/login",
    tags = ["Users"]
)

api_router.include_router(
    token_paths.router,
    prefix = "/login",
    tags = ["Login"]
)

api_router.include_router(
    admin_paths.router,
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(get_current_active_user)],
    responses={418: {"description": "I'm a teapot"}},
)