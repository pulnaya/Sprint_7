import allure
from methods.order_methods import OrderMethods

class TestGetOrdersList:
    order_methods = OrderMethods()

    @allure.title('Получение списка всех заказов')
    def test_get_orders_list_returns_array(self):
        response = self.order_methods.get_orders_list()
    
        assert response.status_code == 200 and "orders" in response.json()
    