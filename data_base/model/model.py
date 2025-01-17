from sqlmodel import Field, SQLModel,create_engine, Relationship
from typing import Optional
from datetime import date
from decimal import Decimal
class Subscribe(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor:Decimal

class Paymodel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscribe_id:int = Field(foreign_key='subscribe.id')
    subscription: Subscribe = Relationship()
    date:date