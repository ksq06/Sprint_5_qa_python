from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helpers.helpers import wait_for_element_login, login, check_main_page
from web_locators.locators import *
from data.urls import Urls
from data.data import PersonData

class TestStellarBurgersLoginLogoutForm:


    def test_login_correct_email_and_password_show_main_page(self, login):
        """При вводе корректных данных отображается основная страничка"""
        driver = login
        check_main_page(driver)

    def test_login_sign_in_button_show_login_page(self, driver):
        """Проверка входа через кнопку 'Войти в аккаунт'"""
        driver.find_element(*MainPage.mn_auth).click()
        wait_for_element_login(driver, AuthLogin.al_login_text)
        login(driver)
        check_main_page(driver)

    def test_login_personal_account_button_show_login_page(self, driver):
        """Проверка входа через кнопку 'Личный Кабинет'"""
        driver.find_element(*MainPage.mn_profile_button).click()
        wait_for_element_login(driver, AuthLogin.al_login_text)
        login(driver)
        check_main_page(driver)

    def test_login_registration_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме регистрации"""
        driver.get(Urls.url_register)
        driver.find_element(*AuthLogin.al_login_text_with_href).click()
        wait_for_element_login(driver, AuthLogin.al_login_text)
        login(driver)
        check_main_page(driver)

    def test_login_forgot_password_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме 'Восстановление пароля'"""
        driver.get(Urls.url_forgot_password)
        driver.find_element(*AuthPassword.ap_login_text_with_href).click()
        wait_for_element_login(driver, AuthLogin.al_login_text)
        login(driver)
        check_main_page(driver)

    def test_logout(self, driver):
        """Проверка выхода из аккаунта"""
        driver.find_element(*MainPage.mn_profile_button).click()
        wait_for_element_login(driver, AuthLogin.al_login_text)
        login(driver)
        check_main_page(driver)

        driver.find_element(*MainPage.mn_profile_button).click()
        logout_button = wait_for_element_login(driver, Navigatorprofile.np_logout_button)
        logout_button.click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.url_login))
        login_button = wait_for_element_login(driver, AuthLogin.al_element_with_login_text)
        assert login_button.text == 'Вход'