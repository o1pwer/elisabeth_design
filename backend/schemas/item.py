import base64
from typing import List, Annotated

from fastapi import UploadFile, File, Form
from pydantic import BaseModel


class CreateItemResponse(BaseModel):
    message: str
    item_id: int


class GetItemsResponse(BaseModel):
    items: list[dict]


class CreateCollectionResponse(BaseModel):
    message: str
    collection_id: int


class Collection(BaseModel):
    name: str
    desc: str
    photos: list[str]


class Item(BaseModel):
    name: str
    desc: str
    collection_id: int
    photos: list[str]
