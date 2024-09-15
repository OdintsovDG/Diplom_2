from faker import Faker


fake = Faker()


def generation_email():
    gen_email = fake.email(8, "yandex.ru")
    return gen_email


def generation_password():
    gen_password = fake.password()
    return gen_password


def generation_name():
    gen_name = fake.user_name()
    return gen_name
