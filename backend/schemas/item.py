from fastapi import Query
from pydantic import BaseModel


class CreateItemResponse(BaseModel):
    message: str
    item_id: int


class UpdateItemResponse(CreateItemResponse):
    pass


class GetItemsResponse(BaseModel):
    items: list[dict] | None


class CreateCollectionResponse(BaseModel):
    message: str
    collection_id: int


class UpdateCollectionResponse(CreateCollectionResponse):
    pass


class DeleteItemResponse(BaseModel):
    message: str
    item_id: int


class DeleteCollectionResponse(BaseModel):
    message: str
    collection_id: int


class Collection(BaseModel):
    name: str
    desc: str
    photos: list[str] | None


class Item(BaseModel):
    name: str
    desc: str
    collection_id: int
    photos: list[str] | None


class UpdateItem(BaseModel):
    name: str | None = None
    desc: str | None = None
    collection_id: int | None = None
    photos: list[str] | None = None
    replace_images: bool = Query(False, description="Set to true to replace all images")


class UpdateCollection(BaseModel):
    name: str | None = None
    desc: str | None = None
    photos: list[str] | None = None
    replace_images: bool = Query(False, description="Set to true to replace all images")
