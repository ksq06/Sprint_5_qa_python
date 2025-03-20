import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData

class TestStellarBurgersRegistration:

    def _go_to_registration_page(self, driver):
        """Переход на страницу регистрации"""
        driver.get(Urls.url_register)

    def _fill_registration_form(self, driver, name, email, password):
        """Заполнение формы регистрации"""
        driver.find_element(*AuthRegister.ar_name_field).send_keys(name)
        driver.find_element(*AuthRegister.ar_email_field).send_keys(email)
        driver.find_element(*AuthRegister.ar_password_field).send_keys(password)

    def _submit_registration_form(self, driver):
        """Нажатие кнопки 'Зарегистрироваться'"""
        driver.find_element(*AuthRegister.ar_register_button).click()

    def _wait_for_element(self, driver, locator, timeout=10):
        """Ожидание появления элемента на странице"""
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Элемент {locator} не найден на странице")

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        """При успешной регистрации перебрасывает на страницу входа"""
        self._go_to_registration_page(driver)
        self._fill_registration_form(driver, ValidData.user_name, ValidData.login, ValidData.password)
        self._submit_registration_form(driver)
        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.url_login))
        login_button = self._wait_for_element(driver, AuthLogin.al_element_with_login_text)

        assert driver.current_url == Urls.url_login
        assert login_button.text == 'Вход'
        driver.quit()

    def test_registration_empty_name_nothing_happens(self, driver):
        """При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет"""
        self._go_to_registration_page(driver)
        self._fill_registration_form(driver, "", "test1@example.ru", "124567")
        self._submit_registration_form(driver)
        self._wait_for_element(driver, AuthRegister.ar_register_button)
        errors_messages = driver.find_elements(*AuthRegister.ar_error_message)
        assert driver.current_url == Urls.url_register
        assert len(errors_messages) == 0
        driver.quit()

    @pytest.mark.parametrize('email_list', [
        'test1@exru', 'test2example.ru', 'te st3@example.ru', 'test4@ex ample.ru',
        '@example.ru', 'test6@.ru', 'test7@example.'
    ])
    def test_registration_incorrect_email_show_error(self, driver, email_list):
        """При некорректном email появляется ошибка, что пользователь уже существует"""
        self._go_to_registration_page(driver)
        self._fill_registration_form(driver, "Рита Морозова", email_list, "123456")
        self._submit_registration_form(driver)
        error_message = self._wait_for_element(driver, AuthRegister.ar_error_message_2)
        assert error_message.text == 'Такой пользователь уже существует'
        driver.quit()

    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_registration_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        """При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'"""
        self._go_to_registration_page(driver)
        self._fill_registration_form(driver, "Рита Морозова", "test1@example.ru", password_list)
        self._submit_registration_form(driver)
        error_message = self._wait_for_element(driver, AuthRegister.ar_error_message)
        assert error_message.text == 'Некорректный пароль'
        driver.quit()