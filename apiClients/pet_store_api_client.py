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
        response = self.session.get(
            url=f'{self.base_url}/pet/findByStatus',
            params=query
        )
        return response

    def create_pet(self, data_json):
        response = self.session.post(
            url=f'{self.base_url}/pet',
            json=data_json
        )
        return response

    def update_or_create_pet(self, data_json):
        response = self.session.put(
            url=f'{self.base_url}/pet',
            json=data_json
        )
        return response

    def get_pet_by_id(self, pet_id: int):
        response = self.session.get(
            url=f'{self.base_url}/pet/{pet_id}',
        )
        return response

    def update_pet_by_id(self, pet_id: int):
        response = self.session.post(
            url=f'{self.base_url}/pet/{pet_id}',
        )
        return response

    def del_pet_by_id(self, pet_id: int):
        response = self.session.delete(
            url=f'{self.base_url}/pet/{pet_id}',
        )
        return response
