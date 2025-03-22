import random


class PersonData:
    user_name = 'Евгений Онегин'
    login = 'evgenonegin@example.ru'
    password = '123456'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@example.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"


class RegistrationData:
    """Тестовые данные для регистрации"""

    valid_name = "Рита Морозова"
    valid_email = "test1@example.ru"
    valid_password = "123456"

    invalid_name = ""
    invalid_email = "test_invalid_email"
    invalid_password = "1"
    invalid_email_list = [
        'test1@exru',
        'test2example.ru',
        'te st3@example.ru',
        'test4@ex ample.ru',
        '@example.ru',
        'test6@.ru',
        'test7@example.'
    ]
    invalid_password_list = [
        '1',
        '12345',
    ]