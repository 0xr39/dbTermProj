from fastapi import FastAPI
from app.controllers.db import router as db_router
app = FastAPI()


app.include_router(db_router, prefix="/db")