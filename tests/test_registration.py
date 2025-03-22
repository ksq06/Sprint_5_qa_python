import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helpers.helpers import go_to_registration_page, fill_registration_form, submit_registration_form, wait_for_element_registration
from helpers.helpers import wait_for_element_registration
from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData, RegistrationData

class TestStellarBurgersRegistration:

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        """При успешной регистрации перебрасывает на страницу входа"""
        go_to_registration_page(driver)
        fill_registration_form(driver, ValidData.user_name, ValidData.login, ValidData.password)
        submit_registration_form(driver)

        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.url_login))
        login_button = wait_for_element_registration(driver, AuthLogin.al_element_with_login_text)

        assert driver.current_url == Urls.url_login
        assert login_button.text == 'Вход'

    def test_registration_empty_name_nothing_happens(self, driver):
        """При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет"""
        go_to_registration_page(driver)
        fill_registration_form(driver, RegistrationData.invalid_name, "test1@example.ru", "124567")
        submit_registration_form(driver)
        wait_for_element_registration(driver, AuthRegister.ar_register_button)

        errors_messages = driver.find_elements(*AuthRegister.ar_error_message)
        assert driver.current_url == Urls.url_register
        assert len(errors_messages) == 0

    @pytest.mark.parametrize('email_list', RegistrationData.invalid_email_list)
    def test_registration_incorrect_email_show_error(self, driver, email_list):
        """При некорректном email появляется ошибка, что пользователь уже существует"""
        go_to_registration_page(driver)
        fill_registration_form(driver, "Рита Морозова", email_list, "123456")
        submit_registration_form(driver)

        error_message = wait_for_element_registration(driver, AuthRegister.ar_error_message_2)
        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password_list', RegistrationData.invalid_password_list)
    def test_registration_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        """При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'"""
        go_to_registration_page(driver)
        fill_registration_form(driver, "Рита Морозова", "test1@example.ru", password_list)
        submit_registration_form(driver)

        error_message = wait_for_element_registration(driver, AuthRegister.ar_error_message)
        assert error_message.text == 'Некорректный пароль'