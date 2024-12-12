import requests


class PerStoreApiClient():

    def __init__(self,
                 base_url="https://petstore.swagger.io/v2",
                 token="special-key"):
        self.session = requests.session()
        self.base_url = base_url
        self.session.headers = {
            "Authorization": f"{token}",
            "Content-Type": "application/json"
        }

    def get_pets_by_status(self, query):
        """Получает питомца по статусу"""
        response = self.session.get(
            url=f'{self.base_url}/pet/findByStatus',
            params=query
        )
        return response

    def create_pet(self, data_json):
        """Создаёт питомца"""
        response = self.session.post(
            url=f'{self.base_url}/pet',
            json=data_json
        )
        return response

    def update_or_create_pet(self, data_json):
        """Обновляет или создаёт питомца"""
        response = self.session.put(
            url=f'{self.base_url}/pet',
            json=data_json
        )
        return response

    def get_pet_by_id(self, pet_id: int):
        """Получает питомца по ID"""
        response = self.session.get(
            url=f'{self.base_url}/pet/{pet_id}',
        )
        return response

    def update_pet_by_id(self, pet_id: int, query):
        """Обновляет питомца по ID"""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = self.session.post(
            url=f'{self.base_url}/pet/{pet_id}',
            data=query,
            headers=headers
        )
        return response

    def del_pet_by_id(self, pet_id: int):
        """Удаляет питомца по ID"""
        response = self.session.delete(
            url=f'{self.base_url}/pet/{pet_id}'
        )
        return response
