from fastapi import APIRouter
from models.item import Item

router = APIRouter(prefix="/items", tags=["Items"])

items = []
@router.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):