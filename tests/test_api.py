from random import choice

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


@pytest.mark.smoke
# в идеале опрашивать из базы , будем получать всегда существ id
# и сможем сверять данные
@pytest.mark.parametrize("pet_id", [id_ for id_ in range(7, 9, 1)])
def test_update_pet_by_id(client_api, need_faker, pet_id):
    """Тест проверяет возможность обновления данных питомца по ID"""
    query = {
        "status": choice([stat.value for stat in PetStatus]),
        "name": need_faker.first_name()
    }
    response = client_api.update_pet_by_id(pet_id=pet_id, query=query)
    assert response.status_code == 200, (
        "Ожидался 200 статус код"
    )
    get_upd_pet_response = client_api.get_pet_by_id(pet_id)
    json_response_get = get_upd_pet_response.json()
    assert get_upd_pet_response.status_code == 200, (
        "Ожидался 200 статус код"
    )
    assert json_response_get, (
        "Ожидалось тело ответа"
    )
    get_upd_pet = Pet.parse_obj(json_response_get)
    assert get_upd_pet.status == query["status"], (
        "status не соответсвует выбранному"
    )
    assert get_upd_pet.name == query["name"], (
        "name не соответсвует выбранному"
    )


@pytest.mark.smoke
# в идеале опрашивать из базы , будем получать всегда существ id
# и сможем сверять данные
@pytest.mark.parametrize("pet_id", [id_ for id_ in range(7, 9, 1)])
def test_get_pet_by_id(client_api, pet_id):
    """Тест проверяет возможность поиска питомца по ID"""
    response = client_api.get_pet_by_id(pet_id=pet_id)
    assert response.status_code == 200, "Ожидался 200 статус код"
    json_response = response.json()
    assert json_response, "Ожидалось тело ответа"
    pet = Pet.parse_obj(json_response)
    assert pet.id == pet_id, "ID не соответствует искомому"
