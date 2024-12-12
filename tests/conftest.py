import pytest

from faker import Faker
from PetStoreTestProj.apiClients.pet_store_api_client import PerStoreApiClient


@pytest.fixture(scope="class")
def client_api():
    """Создаёт клиента для работы с эндпоинтом"""
    client = PerStoreApiClient()
    return client


@pytest.fixture(scope="class")
def need_faker():
    """Создаёт клиента для работы с эндпоинтом"""
    fake = Faker()
    return fake


@pytest.fixture(scope="session")
def db_session():
    """
        Создает сессию БД перед тестами
        и закрывает ее по завершению
    """
    # db = open
    # yield db
    # db.close
