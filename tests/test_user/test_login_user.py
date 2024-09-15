import requests
import helpers
import allure
from data import *


class TestLoginUser:

    @allure.title('Проверка авторизации пользователя. Все обязательные поля заполнены корректно.'
                  'Ручка /api/auth/login')
    def test_login_user_basic_true(self, creation_user):
        code_response = creation_user[4]
        body_response = creation_user[3]
        assert code_response == 200 and 'accessToken' in body_response, (
            f'Status code is {code_response}, body={body_response}'
        )
        print(code_response)
        print(body_response)

    @allure.title('Проверка авторизации несуществующего пользователя. Все обязательные поля заполнены.'
                  'Ручка /api/auth/login')
    def test_login_fake_user_error(self):
        data_user = {'email': helpers.generation_email(), 'password': helpers.generation_password()}
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_LOGIN_USER}', json=data_user)
        assert response.status_code == 401 and (
                response.json() == Message.ERROR_NOT_FOUND_USER
        ), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())
