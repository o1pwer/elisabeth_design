from typing import Annotated

from fastapi import APIRouter, Depends

from database import get_db
from models import DatabaseModel, Item
from models.functions.wrapper import DatabaseContext

catalog_router = APIRouter()
@catalog_router.get("clothes/list")
async def show_clothes_list():
    item_db = get_db(Item)
    return await item_db.get_all()

@catalog_router.get("clothes/list/add")
async def add_clothes(name: str, desc: str):
    item_db = get_db(Item)
    await item_db.add()
    return await item_db.get_all()