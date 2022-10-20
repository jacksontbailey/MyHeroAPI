from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from db.repository.users import get_current_active_user
from schemas.security_classes import settings
from internal import admin
from web_scraper.constants import *
from schemas.card_classes import *
from apis.version1 import security_paths,card_paths, token_paths



#https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/
app = FastAPI(
    title= settings.PROJECT_NAME,
    openapi_url= f"{settings.API_V1_STR}/openapi.json"
)


my_middleware = LowerCaseMiddleware()
app.middleware("http")(my_middleware)


app.include_router(
    security_paths.router,
    prefix="/users",
    tags=["security"],
)

app.include_router(
    card_paths.router,
    prefix = "/v1",
    dependencies= [Depends(get_current_active_user)]
)

app.include_router(
    token_paths.router,
    prefix = "/token",
)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_current_active_user)],
    responses={418: {"description": "I'm a teapot"}},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ORIGINS,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"Greeting": "Welcome to the My Hero Academia Card Game API! This is a fan-made API that any developer is free to use. The only thing I ask is that you give me some credit when you use it, and/or buy me a coffee. This carbon-based lifeform needs Java installed..."}

# -- uvicorn main:app --reload