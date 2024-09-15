import requests
import allure
from data import *


class TestReceivingUserOrders:

    @allure.title('Проверка получения заказов конкретного пользователя.'
                  'Пользователь авторизован, данные ингредиентов корректны.'
                  'Ручка /api/orders')
    def test_receiving_user_orders_with_authorization_true(self, creation_two_order_for_user):
        token = creation_two_order_for_user
        response = requests.get(f'{Url.MAIN_URL}{Url.GET_USER_ORDERS}', headers={'Authorization': token})
        assert response.status_code == 200 and response.json()['success'] is True, (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())

    @allure.title('Проверка невозможности получения заказов конкретного пользователя.'
                  'Пользователь не авторизован, данные ингредиентов корректны.'
                  'Ручка /api/orders')
    def test_receiving_user_orders_without_authorization_true(self, creation_two_order_for_user):
        response = requests.get(f'{Url.MAIN_URL}{Url.GET_USER_ORDERS}')
        assert response.status_code == 401 and response.json() == Message.ERROR_SHOULD_BE_AUTHORIZATION, (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())
