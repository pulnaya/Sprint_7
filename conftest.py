import pytest
from helpers import generate_random_string, generate_order_payload
from methods.couirier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def courier_payload():
    """Фикстура генерирует payload для создания курьера."""
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

@pytest.fixture
def create_and_delete_courier(courier_payload):
    """
    Фикстура создает курьера в системе перед тестом и гарантированно удаляет его после.
    Возвращает кортеж: (response_from_create, courier_payload, courier_id).
    """
    courier_methods = CourierMethods()
    
    create_response = courier_methods.create_courier(courier_payload)
    
    login_payload = {
        "login": courier_payload["login"],
        "password": courier_payload["password"]
    }
    login_response = courier_methods.login_courier(login_payload)
    courier_id = login_response.json().get("id") if login_response.status_code == 200 else None
    
    yield (create_response, courier_payload, courier_id)
    
    if courier_id:
        courier_methods.delete_courier(courier_id)

@pytest.fixture
def order_payload():
    """Фикстура возвращает дефолтный payload для заказа."""
    return generate_order_payload()

@pytest.fixture
def create_order(order_payload):
    """
    Фикстура создает заказ и возвращает его track number.
    """
    order_methods = OrderMethods()
    response = order_methods.create_order(order_payload)
    track = response.json()["track"]
    return track 