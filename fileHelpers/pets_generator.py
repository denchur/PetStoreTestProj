from faker import Faker
from random import choice, randint
from typing import Optional

from PetStoreTestProj.schemas.schemas import Category, Tag, Pet, PetStatus

fake = Faker()

# Количество создаваемых объектов Pet
NUM_PETS = 10

pets_status = [status.value for status in PetStatus]


def create_category() -> Optional[Category]:
    """Согдаёт категорию или оставляет её пустой"""
    if choice([True, False]):
        return Category(
            id=randint(1, 100),
            name=fake.word()
        )
    return None


def create_tags() -> Optional[list[Tag]]:
    """Согдаёт теги или оставляет их пустыми"""
    if choice([True, False]):
        return [
            Tag(id=randint(1, 100), name=fake.word())
            for _ in range(randint(1, 5))
        ]
    return None


def create_pet() -> Pet:
    """Создаёт объект класса Pet"""
    return Pet(
        category=create_category(),
        name=fake.first_name(),
        photoUrls=[fake.image_url() for _ in range(randint(1, 3))],
        tags=create_tags(),
        status=choice(pets_status)
    )


def create_pets() -> list[Pet]:
    """Создаёт список питомцев в количестве NUM_PETS"""
    pets_data = [create_pet() for _ in range(NUM_PETS)]
    return pets_data
