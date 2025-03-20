from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from web_locators.locators import *
from data.urls import Urls
from data.data import PersonData

class TestStellarBurgersLoginLogoutForm:

    def _wait_for_element(self, driver, locator, timeout=10):
        """Ожидание появления элемента на странице"""
        try:
            return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Элемент {locator} не найден на странице")

    def _login(self, driver):
        """Авторизация пользователя"""
        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)
        driver.find_element(*AuthLogin.al_login_button_any_forms).click()

    def _check_main_page(self, driver):
        """Проверка, что пользователь на главной странице"""
        order_button = self._wait_for_element(driver, MainPage.mn_order_button)
        assert driver.current_url == Urls.url_main_page
        assert order_button.text == 'Оформить заказ'

    def test_login_correct_email_and_password_show_main_page(self, login):
        """При вводе корректных данных отображается основная страничка"""
        driver = login
        self._check_main_page(driver)
        driver.quit()

    def test_login_sign_in_button_show_login_page(self, driver):
        """Проверка входа через кнопку 'Войти в аккаунт'"""
        driver.find_element(*MainPage.mn_auth).click()
        self._wait_for_element(driver, AuthLogin.al_login_text)
        self._login(driver)
        self._check_main_page(driver)
        driver.quit()

    def test_login_personal_account_button_show_login_page(self, driver):
        """Проверка входа через кнопку 'Личный Кабинет'"""
        driver.find_element(*MainPage.mn_profile_button).click()
        self._wait_for_element(driver, AuthLogin.al_login_text)
        self._login(driver)
        self._check_main_page(driver)
        driver.quit()

    def test_login_registration_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме регистрации"""
        driver.get(Urls.url_register)
        driver.find_element(*AuthLogin.al_login_text_with_href).click()
        self._wait_for_element(driver, AuthLogin.al_login_text)
        self._login(driver)
        self._check_main_page(driver)
        driver.quit()

    def test_login_forgot_password_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме 'Восстановление пароля'"""
        driver.get(Urls.url_forgot_password)
        driver.find_element(*AuthPassword.ap_login_text_with_href).click()
        self._wait_for_element(driver, AuthLogin.al_login_text)
        self._login(driver)
        self._check_main_page(driver)
        driver.quit()

    def test_logout(self, driver):
        """Проверка выхода из аккаунта"""
        driver.find_element(*MainPage.mn_profile_button).click()
        self._wait_for_element(driver, AuthLogin.al_login_text)
        self._login(driver)
        self._check_main_page(driver)

        driver.find_element(*MainPage.mn_profile_button).click()
        logout_button = self._wait_for_element(driver, Navigatorprofile.np_logout_button)
        logout_button.click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.url_login))
        login_button = self._wait_for_element(driver, AuthLogin.al_element_with_login_text)
        assert login_button.text == 'Вход'
        driver.quit()