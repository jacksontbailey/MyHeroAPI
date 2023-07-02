import uvicorn
from apis.base import api_router
from core.config import settings
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from schemas.schema_card import *
from web_scraper.constants import *


def include_router(app):
	app.include_router(api_router)

def include_middleware(app):

    app.add_middleware(
        CORSMiddleware,
        allow_origins = settings.ORIGINS,
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )


def start_application():
    app = FastAPI(
        title = settings.PROJECT_NAME,
        version = settings.PROJECT_VERSION
    )
    include_middleware(app)
    include_router(app)

    @app.get("/", status_code=status.HTTP_200_OK, tags=['root'])
    async def home():
        return {"Greeting": "Welcome to the My Hero Academia Card Game API! This is a fan-made API that any developer is free to use. The only thing I ask is that you give me some credit when you use it, and/or buy me a coffee. This carbon-based lifeform needs Java installed..."}
    
    return app



app_start = start_application()

if __name__ == "__main__":
    uvicorn.run("main:app_start", host="0.0.0.0", port=8001, reload=True)
# -- uvicorn main:app_start --reload