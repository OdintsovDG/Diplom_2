import requests
import allure
from data import *


class TestCreationOrder:

    @allure.title('Проверка создания заказа. Пользователь авторизован, данные ингредиентов корректны.'
                  'Ручка /api/orders')
    def test_creation_order_with_authorization_true(self, creation_user):
        token = creation_user[7]
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_ORDER}',
                                 headers={'Authorization': token}, data=ForBurger.INGREDIENTS)
        assert response.status_code == 200 and response.json()['success'] is True, (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())

    @allure.title('Проверка создания заказа. Пользователь не авторизован, данные ингредиентов корректны.'
                  'Ручка /api/orders')
    def test_creation_order_without_authorization_true(self):
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_ORDER}', data=ForBurger.INGREDIENTS)
        assert response.status_code == 200 and response.json()['success'] is True, (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())

    @allure.title('Проверка невозможности создания заказа. Пользователь не авторизован, ингредиенты отсутствуют.'
                  'Ручка /api/orders')
    def test_creation_order_without_authorization_and_ingredients_error(self):
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_ORDER}')
        assert response.status_code == 400 and response.json() == Message.ERROR_NOT_FOUND_INGREDIENTS, \
            f'Status code is {response.status_code}, body={response.json()}'
        print(response.status_code)
        print(response.json())

    @allure.title('Проверка невозможности создания заказа. '
                  'Пользователь не авторизован, хэш ингредиента передан с ошибкой.'
                  'Ручка /api/orders')
    def test_creation_order_without_authorization_and_error_hash_ingredients_error(self):
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_ORDER}', data=ForBurger.ERROR_INGREDIENTS)
        assert response.status_code == 400 and response.json() == Message.ERROR_INTERNAL_SERVER, \
            f'Status code is {response.status_code}, body={response.json()}'
        print(response.status_code)
        print(response.json())
