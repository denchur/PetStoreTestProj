import pytest

from PetStoreTestProj.apiClients.pet_store_api_client import PerStoreApiClient


@pytest.fixture(scope="class")
def client_api():
    client = PerStoreApiClient()
    return client
