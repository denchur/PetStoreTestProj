from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Category(BaseModel):
    id: int
    name: Optional[str] = ""


class Tag(BaseModel):
    id: int
    name: Optional[str] = ""


class PetStatus(Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class Pet(BaseModel):
    id: Optional[int] = None
    category: Optional[Category] = None
    name: Optional[str] = ""
    photoUrls: list[str]
    tags: Optional[list[Tag]] = None
    status: PetStatus

    class Config:
        use_enum_values = True
