from fastapi import APIRouter
from models.item import Item

router = APIRouter(prefix="/items", tags=["Items"])

items = []
@router.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    pass

@router.get("/items")
async def list_items():
    pass

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    pass