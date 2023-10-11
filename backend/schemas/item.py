import base64

from fastapi import Query
from pydantic import BaseModel, field_validator

from exceptions.validation import InvalidBase64StringError


class Base64PhotosMixin:
    @field_validator('photos', mode='before', check_fields=True)
    def validate_base64_strings(cls, value):
        if value is None:
            return value  # If the list is None, it's considered valid

        for string in value:
            try:
                # Attempt to decode each string as Base64
                base64.b64decode(string)
            except Exception as e:
                raise InvalidBase64StringError(f'Invalid Base64 string: {string}') from e

        return value


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


class Collection(BaseModel, Base64PhotosMixin):
    name: str
    desc: str
    photos: list[str] | None


class Item(BaseModel, Base64PhotosMixin):
    name: str
    desc: str
    collection_id: int
    photos: list[str] | None


class UpdateItem(BaseModel, Base64PhotosMixin):
    name: str | None = None
    desc: str | None = None
    collection_id: int | None = None
    photos: list[str] | None = None
    replace_images: bool = Query(False, description="Set to true to replace all images")


class UpdateCollection(BaseModel, Base64PhotosMixin):
    name: str | None = None
    desc: str | None = None
    photos: list[str] | None = None
    replace_images: bool = Query(False, description="Set to true to replace all images")
