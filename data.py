class Url:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    POST_CREATION_USER = 'api/auth/register'
    POST_LOGIN_USER = 'api/auth/login'
    GET_DATA_USER = 'api/auth/user'
    PATH_DATA_USER = 'api/auth/user'
    DELETE_USER = 'api/auth/user'
    POST_CREATION_ORDER = 'api/orders'
    GET_USER_ORDERS = 'api/orders'


class Message:
    ERROR_DOUBLE_USER = {'message': 'User already exists', 'success': False}
    ERROR_REQUIRED_FIELDS_NOT_FILLED = {'message': 'Email, password and name are required fields', 'success': False}
    ERROR_NOT_FOUND_USER = {'message': 'email or password are incorrect', 'success': False}
    ERROR_SHOULD_BE_AUTHORIZATION = {'message': 'You should be authorised', 'success': False}
    ERROR_NOT_FOUND_INGREDIENTS = {'success': False, 'message': 'Ingredient ids must be provided'}
    ERROR_INTERNAL_SERVER = {'success': False, 'message': 'One or more ids provided are incorrect'}


class ForBurger:
    INGREDIENTS = {'ingredients': ['61c0c5a71d1f82001bdaaa6c', '61c0c5a71d1f82001bdaaa6e', '61c0c5a71d1f82001bdaaa73']}
    ERROR_INGREDIENTS = {'ingredients': ['61c0c5a7000000000bdaaa6c']}
    INGREDIENTS_TWO = {'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f',
                                       '61c0c5a71d1f82001bdaaa72']}
