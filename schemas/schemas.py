from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Category(BaseModel):
    """Схема для сериализации/десериализации категории"""
    id: int
    name: Optional[str] = ""


class Tag(BaseModel):
    """Схема для сериализации/десериализации тегов"""
    id: int
    name: Optional[str] = ""


class PetStatus(Enum):
    """Enum статусов питомцев"""
    available = "available"
    pending = "pending"
    sold = "sold"


class Pet(BaseModel):
    """Схема для сериализации/десериализации питомцев"""
    id: Optional[int] = None
    category: Optional[Category] = None
    name: Optional[str] = ""
    photoUrls: list[str]
    tags: Optional[list[Tag]] = None
    status: PetStatus

    class Config:
        use_enum_values = True
