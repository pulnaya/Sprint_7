import allure
import requests
from data import BASE_URL, ORDERS_URL

class OrderMethods:
    def __init__(self):
        self.base_url = BASE_URL
        self.orders_url = ORDERS_URL

    @allure.step('Создать заказ')
    def create_order(self, payload):
        response = requests.post(
            f"{self.base_url}{self.orders_url}", 
            json=payload
        )
        return response

    @allure.step('Получить список всех заказов')
    def get_orders_list(self):
        response = requests.get(
            f"{self.base_url}{self.orders_url}"
        )
        return response