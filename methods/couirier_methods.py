import requests
import allure
from data import BASE_URL, COURIER_URL

class CourierMethods:
    def __init__(self):
        self.base_url = BASE_URL
        self.courier_url = COURIER_URL

    @allure.step('Создать курьера')
    def create_courier(self, payload):
        response = requests.post(
            f"{self.base_url}{self.courier_url}", 
            json=payload # Важно! Используем json= для отправки словаря как JSON
        )
        return response

    @allure.step('Авторизоваться курьером')
    def login_courier(self, payload):
        response = requests.post(
            f"{self.base_url}{self.courier_url}/login", 
            json=payload
        )
        return response

    @allure.step('Удалить курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(
            f"{self.base_url}{self.courier_url}/{courier_id}"
        )
        return response