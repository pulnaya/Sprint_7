import allure
from methods.couirier_methods import CourierMethods
from helpers import generate_random_string
from data import LOGIN_WRONG_CREDENTIALS, LOGIN_INSUFFICIENT_DATA

class TestCourierLogin:
    courier_methods = CourierMethods()

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, create_and_delete_courier):
        _, courier_payload, _ = create_and_delete_courier
        
        login_payload = {
            "login": courier_payload["login"],
            "password": courier_payload["password"]
        }
    
        response = self.courier_methods.login_courier(login_payload)
        
        assert response.status_code == 200 and "id" in response.json()

    @allure.title('Авторизация с неверным паролем')
    def test_login_courier_with_wrong_password(self, create_and_delete_courier):
        _, courier_payload, _ = create_and_delete_courier
        
        login_payload = {
            "login": courier_payload["login"],
            "password": "wrong_password_123"  # Неверный пароль
        }
        
        response = self.courier_methods.login_courier(login_payload)
        
        assert response.status_code == 404 and response.json()["message"] == LOGIN_WRONG_CREDENTIALS

    @allure.title('Авторизация под несуществующим пользователем')
    def test_login_nonexistent_courier(self):
        login_payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        
        response = self.courier_methods.login_courier(login_payload)
        
        assert response.status_code == 404 and response.json()["message"] == LOGIN_WRONG_CREDENTIALS


    @allure.title('Авторизация с пустым паролем')
    def test_login_courier_empty_password(self, create_and_delete_courier):
        _, courier_payload, _ = create_and_delete_courier
        login_payload = {
            "login": courier_payload["login"],
            "password": ""  
        }
        
        response = self.courier_methods.login_courier(login_payload)
        
        assert response.status_code == 400 and response.json()["message"] == LOGIN_INSUFFICIENT_DATA

    @allure.title('Авторизация без передачи логина')
    def test_login_courier_missing_login(self, create_and_delete_courier):
        _, courier_payload, _ = create_and_delete_courier
        
        login_payload = {
            "password": courier_payload["password"]
        }
        
        response = self.courier_methods.login_courier(login_payload)
        
        assert response.status_code == 400 and response.json()["message"] == LOGIN_INSUFFICIENT_DATA

    @allure.title('Авторизация с пустым логином')
    def test_login_courier_empty_login(self, create_and_delete_courier):
        _, courier_payload, _ = create_and_delete_courier
        
        login_payload = {
            "login": "",
            "password": courier_payload["password"]
        }
        response = self.courier_methods.login_courier(login_payload)
        
        # Проверяем ошибку
        assert response.status_code == 400 and response.json()["message"] == LOGIN_INSUFFICIENT_DATA