import allure
import pytest
from methods.couirier_methods import CourierMethods
from helpers import  generate_random_string

class TestCreateCourier:
    courier_methods = CourierMethods()

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, create_and_delete_courier):
        
        response, payload, _ = create_and_delete_courier
        
        assert response.status_code == 201 and response.json()["ok"] ==  True


    @allure.title('Создание двух одинаковых курьеров')
    def test_create_duplicate_courier(self, create_and_delete_courier):
       
        _, payload, _ = create_and_delete_courier
        
        response = self.courier_methods.create_courier(payload)

        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Нельзя создать курьера с уже существующим логином')
    def test_create_courier_with_existing_login(self, create_and_delete_courier):
    
        _, existing_payload, _ = create_and_delete_courier
        duplicate_login_payload = {
            "login": existing_payload["login"],
            "password": generate_random_string(10), 
            "firstName": generate_random_string(10)
        }
        
        response = self.courier_methods.create_courier(duplicate_login_payload)
        
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    
    @allure.title('Создание курьера без обязательного поля')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_without_required_field(self, courier_payload, missing_field):
        test_payload = courier_payload.copy()
        del test_payload[missing_field]
        
        response = self.courier_methods.create_courier(test_payload)
        
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"
        