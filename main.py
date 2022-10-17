from fastapi import Depends, FastAPI, Security, status
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


from dependencies.security_funct import get_current_active_user 
from dependencies.security_classes import settings
from internal import admin
from routers import security_paths, card_paths, token_paths
from card_page.constants import *
from card_page.card_classes import *



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

@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """ 

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).carddb

    await init_beanie(
        database=db_client,
        document_models=[]
    )

#@app.post('/signup', summary="Create new user", response_model=UserOut)
#async def create_user(data: UserAuth):
#    user = db.get(data.email, None)

@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"Greeting": "Welcome to the My Hero Academia Card Game API! This is a fan-made API that any developer is free to use. The only thing I ask is that you give me some credit when you use it, and/or buy me a coffee. This carbon-based lifeform needs Java installed..."}


# -- uvicorn main:app --reload