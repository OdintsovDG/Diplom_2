import requests
import helpers
import allure
from data import *
import logging
logging.basicConfig(level=logging.INFO)


class TestChangingUserData:

    @allure.title('Проверка изменения имени пользователя. Все обязательные поля заполнены корректно.'
                  'Ручка /api/auth/user')
    def test_changing_name_with_authorization_user_true(self, creation_user):
        token = creation_user[7]
        new_data_user = {'email': creation_user[6], 'name': helpers.generation_name()}
        response = requests.patch(f'{Url.MAIN_URL}{Url.PATH_DATA_USER}',
                                  headers={'Authorization': token}, json=new_data_user)
        assert response.status_code == 200 and response.json()['success'] is True, (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        logging.info(response.status_code)
        logging.info(response.json())

    @allure.title('Проверка изменения email пользователя. Все обязательные поля заполнены корректно.'
                  'Ручка /api/auth/user')
    def test_changing_email_with_authorization_user_true(self, creation_user):
        token = creation_user[7]
        new_data_user = {'email': helpers.generation_email(), 'name': creation_user[5]}
        response = requests.patch(f'{Url.MAIN_URL}{Url.PATH_DATA_USER}',
                                  headers={'Authorization': token}, json=new_data_user)
        assert response.status_code == 200 and response.json()['success'] is True, (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        logging.info(response.status_code)
        logging.info(response.json())

    @allure.title('Проверка невозможности изменения email и имени пользователя без авторизации.'
                  'Все обязательные поля заполнены корректно. Ручка /api/auth/user')
    def test_changing_email_and_name_without_authorization_user_error(self, creation_user):
        new_data_user = {'email': helpers.generation_email(), 'name': helpers.generation_name()}
        response = requests.patch(f'{Url.MAIN_URL}{Url.PATH_DATA_USER}', json=new_data_user)
        assert (response.status_code == 401 and
                response.json() == Message.ERROR_SHOULD_BE_AUTHORIZATION), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        logging.info(response.status_code)
        logging.info(response.json())
