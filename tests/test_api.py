import pytest

from PetStoreTestProj.schemas.schemas import Pet, PetStatus
from PetStoreTestProj.fileHelpers.pets_generator import create_pets


@pytest.mark.smoke
@pytest.mark.parametrize("pet_status", [status.value for status in PetStatus])
def test_get_pet_by_status(client_api, pet_status):
    """Тест проверяет эндпоинт для поиска питомцев по статусу"""
    query = {"status": pet_status}
    response = client_api.get_pets_by_status(query)
    assert response.status_code == 200, "Ожидался 200 статус код"
    json_response = response.json()
    assert json_response, "Ожидалось тело ответа"
    pets = [Pet.parse_obj(obj) for obj in json_response]
    for pet in pets:
        assert pet.status == pet_status, (
            "Статус не соответствует искомому"
        )


@pytest.mark.smoke
@pytest.mark.parametrize("pet", create_pets())
def test_create_pet(client_api, pet):
    """
        Тест проверяет эндпоинт для создания питомцев
        1) создаёт объект класса Pet на основе случайных данных
        2) отпрвляет объект на эндпоинт
        3) из поолученного ответа получает id питомца
        4) запрошивает созданного питомца по id
        5) сверяет отправленный и полученный объект класса Pet
    """
    created_response = client_api.create_pet(data_json=pet.dict())
    assert created_response.status_code == 200, "Ожидался 200 статус код"
    json_response = created_response.json()
    assert json_response, "Ожидалось тело ответа"
    created_pet = Pet.parse_obj(json_response)
    get_crt_pet_response = client_api.get_pet_by_id(created_pet.id)
    json_response_get = get_crt_pet_response.json()
    assert get_crt_pet_response.status_code == 200, "Ожидался 200 статус код"
    assert json_response_get, "Ожидалось тело ответа"
    get_pet_by_created_id = Pet.parse_obj(json_response_get)
    assert created_pet.name == get_pet_by_created_id.name, (
        "name созданного животного не совпадает с заданным"
    )
    assert created_pet.photoUrls == get_pet_by_created_id.photoUrls, (
        "photoUrls созданного животного не совпадает с заданным"
    )
    assert created_pet.tags == get_pet_by_created_id.tags, (
        "tags созданного животного не совпадает с заданным"
    )
    assert created_pet.category == get_pet_by_created_id.category, (
        "category созданного животного не совпадает с заданным"
    )
    assert created_pet.status == get_pet_by_created_id.status, (
        "category созданного животного не совпадает с заданным"
    )
