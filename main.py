from fastapi import FastAPI

from apps.accounts.routers import router as ac_router
from apps.app.routers import router as app_router
from utils.routers import router as utils_router
from database import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()
app.include_router(ac_router)
app.include_router(app_router)
app.include_router(utils_router)


@app.get("/")
async def index():
    return {"message": "Hello World!"}


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True
)
