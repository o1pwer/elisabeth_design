from fastapi import Query
from pydantic import BaseModel


class CreateItemResponse(BaseModel):
    message: str
    item_id: int


class UpdateItemResponse(CreateItemResponse):
    pass


class GetItemsResponse(BaseModel):
    items: list[dict] | None


class CreateClothesSetResponse(BaseModel):
    message: str
    clothes_set_id: int


class UpdateClothesSetResponse(CreateClothesSetResponse):
    pass


class DeleteItemResponse(BaseModel):
    message: str
    item_id: int


class DeleteClothesSetResponse(BaseModel):
    message: str
    clothes_set_id: int


class ClothesSet(BaseModel):
    name: str
    desc: str
    photos: list[str] | None


class Item(BaseModel):
    name: str
    desc: str
    clothes_set_id: int
    photos: list[str] | None

class Image(BaseModel):
    id: int
    link: str
    clothes_set_id: int
    item_id: int
class UpdateItem(BaseModel):
    name: str | None = None
    desc: str | None = None
    clothes_set_id: int | None = None
    photos: list[str] | None = None
    replace_images: bool = Query(False, description="Set to true to replace all images")


class UpdateClothesSet(BaseModel):
    name: str | None = None
    desc: str | None = None
    photos: list[str] | None = None
    replace_images: bool = Query(False, description="Set to true to replace all images")

class ClothesSetItem(BaseModel):
    id: int
    name: str
    desc: str
    items: list[Item]
    images: list[Image]

class GetClothesSetItemsResponse(BaseModel):

    clothes_sets: list[ClothesSetItem]
    class Config:
        from_attributes = True
