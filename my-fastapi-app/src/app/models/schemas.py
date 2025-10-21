from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tags: List[str] = []

class User(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None
    email: str
    items: List[Item] = []