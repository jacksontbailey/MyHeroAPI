from fastapi import Depends, FastAPI, Security

from routers import card_paths, security_paths

from .dependencies.security_funct import get_current_user 
from .internal import admin
from .routers import cards, users

app = FastAPI(dependencies=[Depends(get_current_user)])


app.include_router(security_paths.router)
app.include_router(card_paths.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Security(get_current_user)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
