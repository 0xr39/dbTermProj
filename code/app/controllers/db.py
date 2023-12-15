from fastapi import APIRouter
from app.models.db_init import db_init
from app.models.db_crud import db_crud

router = APIRouter()

@router.get("/create")
def create_db():
    return db_init.create_db()

@router.get("/getholder/{tokenAddr}")
def getHolder(tokenAddr: str):
    return db_crud.getHolder(tokenAddr)