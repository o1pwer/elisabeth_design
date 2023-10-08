import base64

from fastapi import APIRouter, HTTPException
from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from database import get_db
from exceptions.validation import InvalidBase64StringError
from models import Item, Collection
from models.item import Image
from schemas.item import Collection as CollectionSchema, UpdateItemResponse, UpdateItem, UpdateCollection
from schemas.item import CreateItemResponse, GetItemsResponse, CreateCollectionResponse
from schemas.item import Item as ItemSchema

catalog_router = APIRouter(prefix='/clothes')


@catalog_router.get("/list", response_model=GetItemsResponse)
async def show_clothes_list(request: Request):
    item_db = get_db(Item)
    items = await item_db.get_all()

    # Extract the query parameters from the request
    query_params = dict(request.query_params)

    # Check if any filter parameters were provided
    if not query_params:
        return JSONResponse(
            content={'items': [item.as_dict() for item in items]},
            status_code=status.HTTP_200_OK,
        )

    # Filter the items based on the provided parameters
    filtered_items = items
    for param, value in query_params.items():
        filtered_items = [item for item in filtered_items if getattr(item, param, None) == value]

    # If no items match the filters, return an HTTP 404 response
    if not filtered_items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items match the provided filters")

    return JSONResponse(
        content={'items': [item.as_dict() for item in filtered_items]},
        status_code=status.HTTP_200_OK,
    )


@catalog_router.post("/list/add", response_model=CreateItemResponse)
async def add_clothes(item: ItemSchema):
    item_db = get_db(Item)
    image_db = get_db(Image)
    item_object = await item_db.add(name=item.name, desc=item.desc, collection_id=item.collection_id)
    try:
        for image in item.photos:
            await image_db.add(content=base64.b64decode(image))
    except InvalidBase64StringError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Base64 string.",
        ) from e
    return JSONResponse(
        content={'message': 'Item successfully created.', 'item_id': item_object.id},
        status_code=status.HTTP_201_CREATED,
    )


@catalog_router.post("/collections/add", response_model=CreateCollectionResponse)
async def add_collection(collection: CollectionSchema):
    collection_db = get_db(Collection)
    image_db = get_db(Image)
    collection_object = await collection_db.add(name=collection.name, desc=collection.desc)
    try:
        for image in collection.photos:
            await image_db.add(content=base64.b64decode(image))
    except InvalidBase64StringError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Base64 string.",
        ) from e
    return JSONResponse(
        content={'message': 'Collection successfully created.', 'collection_id': collection_object.id},
        status_code=status.HTTP_201_CREATED,
    )


@catalog_router.put("/list/update/{item_id}", response_model=UpdateItemResponse)
async def update_clothes(item_id: int, item: UpdateItem):
    if not (fields := item.model_dump(exclude={'replace_images', 'photos'}, exclude_none=True)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Provide at least one field to update.")
    item_db = get_db(Item)
    image_db = get_db(Image)
    await item_db.update(Item.id == item_id, **fields)
    if await image_db.exists(Image.item_id == item_id) and item.replace_images:
        await image_db.delete(Image.item_id == item_id)
    if item.photos:
        try:
            for image in item.photos:
                await image_db.add(content=base64.b64decode(image), item_id=item_id)
        except InvalidBase64StringError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Base64 string.",
            ) from e
    return JSONResponse(
        content={'message': 'Item successfully updated', 'item_id': item_id},
        status_code=status.HTTP_200_OK,
    )


@catalog_router.put("/collections/update/{collection_id}", response_model=CreateCollectionResponse)
async def update_collection(collection_id: int, collection: UpdateCollection):
    if not (fields := collection.model_dump(exclude={'replace_images', 'photos'}, exclude_none=True)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Provide at least one field to update.")
    collection_db = get_db(Collection)
    image_db = get_db(Image)
    await collection_db.update(Collection.id == collection_id, **fields)
    if await image_db.exists(Image.collection_id == collection_id) and collection.replace_images:
        await image_db.delete(Image.collection_id == collection_id)
    if collection.photos:
        try:
            for image in collection.photos:
                await image_db.add(content=base64.b64decode(image), collection_id=collection_id)
        except InvalidBase64StringError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Base64 string.",
            ) from e
    return JSONResponse(
        content={'message': 'Collection successfully updated.', 'collection_id': collection_id},
        status_code=status.HTTP_200_OK,
    )
