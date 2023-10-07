import base64

from fastapi import APIRouter, File, UploadFile, Form
from fastapi import status
from fastapi.responses import JSONResponse

from database import get_db
from models import Item, Collection
from models.item import Image
from schemas.item import CreateItemResponse, GetItemsResponse, CreateCollectionResponse
from schemas.item import Collection as CollectionSchema
from schemas.item import Item as ItemSchema

catalog_router = APIRouter(prefix='/clothes')


@catalog_router.get("/list", response_model=GetItemsResponse)
async def show_clothes_list():
    item_db = get_db(Item)
    return JSONResponse(
        content={'items': [item.as_dict() for item in await item_db.get_all()]},
        status_code=status.HTTP_200_OK,
    )


@catalog_router.post("/list/add", response_model=CreateItemResponse)
async def add_clothes(item: ItemSchema):
    item_db = get_db(Item)
    image_db = get_db(Image)
    item_object = await item_db.add(name=item.name, desc=item.desc, collection_id=item.collection_id)
    for image in item.photos:
        await image_db.add(content=base64.b64decode(image))
    return JSONResponse(
        content={'message': 'Item successfully created.', 'item_id': item_object.id},
        status_code=status.HTTP_201_CREATED,
    )


@catalog_router.post("/collection/add", response_model=CreateCollectionResponse)
async def add_collection(collection: CollectionSchema):
    collection_db = get_db(Collection)
    image_db = get_db(Image)
    collection_object = await collection_db.add(name=collection.name, desc=collection.desc)
    for image in collection.photos:
        await image_db.add(content=base64.b64decode(image))
    return JSONResponse(
        content={'message': 'Collection successfully created.', 'collection_id': collection_object.id},
        status_code=status.HTTP_201_CREATED,
    )