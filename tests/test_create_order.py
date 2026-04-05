import allure
import pytest
from methods.order_methods import OrderMethods
from helpers import generate_random_string, generate_order_payload

class TestCreateOrder:
    order_methods = OrderMethods()

    @allure.title('Создание заказа с разными вариантами цветов')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        None  
    ])
    def test_create_order_with_different_colors(self, color):
        payload = generate_order_payload(color)
        response = self.order_methods.create_order(payload)
        assert response.status_code == 201 and "track" in response.json()
    