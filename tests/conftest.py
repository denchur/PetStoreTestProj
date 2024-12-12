import pytest

from PetStoreTestProj.apiClients.pet_store_api_client import PerStoreApiClient


@pytest.fixture(scope="class")
def client_api():
    """Создаёт клиента для работы с эндпоинтом"""
    client = PerStoreApiClient()
    return client
