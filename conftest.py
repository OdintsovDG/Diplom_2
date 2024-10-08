import pytest
import requests
import helpers
from data import *


@pytest.fixture
def creation_user():
    email = helpers.generation_email()  # 6
    password = helpers.generation_password()
    name = helpers.generation_name()  # 5
    data_user = {'email': email, 'password': password, 'name': name}  # 0
    crt_user = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_USER}', json=data_user)  # 1, 2
    authorization = {'email': email, 'password': password}
    login_user = requests.post(f'{Url.MAIN_URL}{Url.POST_LOGIN_USER}', json=authorization)  # 3, 4
    yield (data_user, crt_user.status_code, crt_user.json(),
           login_user.json(), login_user.status_code, name, email, crt_user.json()["accessToken"])
    requests.delete(f'{Url.MAIN_URL}{Url.DELETE_USER}{crt_user.json()["accessToken"]}')


@pytest.fixture()
def creation_two_order_for_user(creation_user):
    token = creation_user[7]
    order = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_ORDER}',
                          headers={'Authorization': token}, data=ForBurger.INGREDIENTS)
    order_two = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_ORDER}',
                              headers={'Authorization': token}, data=ForBurger.INGREDIENTS_TWO)
    yield token
