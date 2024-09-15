import requests
import helpers
import allure
from data import *


class TestsCreationCourier:

    @allure.title('Проверка возможности создания пользователя. Заполнены все обязательные поля.'
                  'Ручка /api/auth/register')
    def test_creation_user_basic_true(self, creation_user):
        code_response = creation_user[1]
        body_response = creation_user[2]
        assert code_response == 200 and (
                'accessToken' in body_response
        ), (
            f'Status code is {code_response}, body={body_response}'
        )
        print(f'\n{code_response}, \n{body_response}')

    @allure.title('Проверка невозможности создания двух одинаковых пользователей. Email, пароль и имя идентичны.'
                  'Ручка /api/auth/register')
    def test_creation_two_full_identical_users_error(self, creation_user):
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_USER}', json=creation_user[0])
        assert response.status_code == 403 and (
                response.json() == Message.ERROR_DOUBLE_USER
        ), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())

    @allure.title('Проверка невозможности создания пользователя. Не заполнено поле "password".'
                  'Ручка /api/auth/register')
    def test_creation_user_incomplete_data_error(self):
        data_courier = {'email': helpers.generation_email(), 'name': helpers.generation_name()}
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_USER}', json=data_courier)
        assert response.status_code == 403 and (
                response.json() == Message.ERROR_REQUIRED_FIELDS_NOT_FILLED
        ), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())
