from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from helpers.helpers import wait_for_element_navigator, go_to_profile, check_profile_page, check_constructor_page
from web_locators.locators import *
from data.urls import Urls

class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        """Открыть личный кабинет"""
        driver = login
        go_to_profile(driver)
        check_profile_page(driver)

    def test_click_constructor_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор'"""
        driver = login
        go_to_profile(driver)
        driver.find_element(*MainPage.mn_constructor_button).click()
        check_constructor_page(driver)

    def test_click_logo_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии на лого"""
        driver = login
        go_to_profile(driver)
        driver.find_element(*MainPage.mn_logo).click()
        check_constructor_page(driver)

    def test_click_logout_button_in_lk_open_login_form(self, login):
        """Выход из аккаунта"""
        driver = login

        go_to_profile(driver)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Navigatorprofile.np_logout_button)).click()

        wait_for_element_navigator(driver, AuthLogin.al_login_button_any_forms)

        assert driver.current_url == Urls.url_login, f"Ожидался URL {Urls.url_login}, но получен {driver.current_url}"

        login_button = wait_for_element_navigator(driver, AuthLogin.al_element_with_login_text)
        assert login_button.text == 'Вход', f"Ожидался текст 'Вход', но получен {login_button.text}"
