from fastapi import APIRouter, HTTPException
from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from database import get_db
from models import Item, ClothesSet
from models.item import Image
from schemas.item import ClothesSet as CollectionSchema, UpdateItemResponse, UpdateItem, UpdateClothesSet, \
    DeleteItemResponse, UpdateClothesSetResponse, DeleteClothesSetResponse, GetClothesSetItemsResponse
from schemas.item import CreateItemResponse, GetItemsResponse, CreateClothesSetResponse
from schemas.item import Item as ItemSchema

catalog_router = APIRouter(prefix='/clothes')


@catalog_router.get("/list", response_model=GetItemsResponse)
async def show_clothes_list(request: Request):
    item_db = get_db(Item)
    items = await item_db.get_all()

    query_params = dict(request.query_params)
    if not query_params:
        return JSONResponse(
            content={'items': [item.as_dict() for item in items]},
            status_code=status.HTTP_200_OK,
        )
    filtered_items = items
    for param, value in query_params.items():
        filtered_items = [item for item in filtered_items if getattr(item, param, None) == value]
    if not filtered_items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No items match the provided filters"
        )

    return JSONResponse(
        content={'items': [item.as_dict() for item in filtered_items]},
        status_code=status.HTTP_200_OK,
    )

@catalog_router.get("/list/clothes_sets", response_model=GetClothesSetItemsResponse)
async def show_clothes_set_list(request: Request):
    clothes_set_db = get_db(ClothesSet)
    clothes_sets = await clothes_set_db.get_all(load=ClothesSet.images)
    query_params = dict(request.query_params)
    if not query_params:
        return JSONResponse(
            content={'clothes_sets': [item.as_dict() for item in clothes_sets]},
            status_code=status.HTTP_200_OK,
        )
    filtered_items = clothes_sets
    for param, value in query_params.items():
        filtered_items = [item for item in filtered_items if getattr(item, param, None) == value]
    if not filtered_items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No items match the provided filters"
        )

    return JSONResponse(
        content={'clothes_sets': [item.as_dict() for item in filtered_items]},
        status_code=status.HTTP_200_OK,
    )
@catalog_router.post("/list/add", response_model=CreateItemResponse)
async def add_clothes(item: ItemSchema):
    item_db = get_db(Item)
    image_db = get_db(Image)

    item_object = await item_db.add(name=item.name, desc=item.desc, clothes_set_id=item.clothes_set_id)
    for image_link in item.photos:
        await image_db.add(link=image_link)
    return JSONResponse(
        content={'message': 'Item successfully created.', 'item_id': item_object.id},
        status_code=status.HTTP_201_CREATED,
    )


@catalog_router.post("/clothes_sets/add", response_model=CreateClothesSetResponse)
async def add_clothes_set(clothes_set: CollectionSchema):
    clothes_set_db = get_db(ClothesSet)
    image_db = get_db(Image)

    clothes_set_object = await clothes_set_db.add(name=clothes_set.name, desc=clothes_set.desc)
    for image_link in clothes_set.photos:
        await image_db.add(link=image_link)
    return JSONResponse(
        content={'message': 'Clothes set successfully created.', 'clothes_set_id': clothes_set_object.id},
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
        for image_link in item.photos:
            await image_db.add(link=image_link, item_id=item_id)
    return JSONResponse(
        content={'message': 'Item successfully updated', 'item_id': item_id},
        status_code=status.HTTP_200_OK,
    )


@catalog_router.put("/clothes_sets/update/{clothes_set_id}", response_model=UpdateClothesSetResponse)
async def update_clothes_set(clothes_set_id: int, clothes_set: UpdateClothesSet):
    if not (fields := clothes_set.model_dump(exclude={'replace_images', 'photos'}, exclude_none=True)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Provide at least one field to update.")

    clothes_set_db = get_db(ClothesSet)
    image_db = get_db(Image)

    await clothes_set_db.update(ClothesSet.id == clothes_set_id, **fields)
    if await image_db.exists(Image.clothes_set_id == clothes_set_id) and clothes_set.replace_images:
        await image_db.delete(Image.clothes_set_id == clothes_set_id)
    if clothes_set.photos:
        for image_link in clothes_set.photos:
            await image_db.add(link=image_link, clothes_set_id=clothes_set_id)
    return JSONResponse(
        content={'message': 'Clothes set successfully updated.', 'clothes_set_id': clothes_set_id},
        status_code=status.HTTP_200_OK,
    )


@catalog_router.delete("/list/delete/{item_id}", response_model=DeleteItemResponse)
async def delete_clothes(item_id: int):
    item_db = get_db(Item)
    image_db = get_db(Image)

    if await item_db.exists(Item.id == item_id):
        await item_db.delete(Item.id == item_id)
        await image_db.delete(Image.item_id == item_id)
        return JSONResponse(
            content={'message': 'Item successfully deleted', 'item_id': item_id},
            status_code=status.HTTP_200_OK,
        )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item was not found.")


@catalog_router.delete("/clothes_sets/update/{clothes_set_id}", response_model=DeleteClothesSetResponse)
async def delete_clothes_set(clothes_set_id: int):
    clothes_set_db = get_db(ClothesSet)
    image_db = get_db(Image)

    if await clothes_set_db.exists(ClothesSet.id == clothes_set_id):
        await clothes_set_db.delete(ClothesSet.id == clothes_set_id)
        await image_db.delete(Image.clothes_set_id == clothes_set_id)
        return JSONResponse(
            content={'message': 'Clothes set successfully deleted', 'clothes_set_id': clothes_set_id},
            status_code=status.HTTP_200_OK,
        )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clothes set was not found.")
