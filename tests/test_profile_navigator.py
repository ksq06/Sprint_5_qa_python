from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from web_locators.locators import *
from data.urls import Urls

class TestStellarBurgersProfileForm:

    def _wait_for_element(self, driver, locator, timeout=10):
        """Ожидание появления элемента на странице"""
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Элемент {locator} не найден на странице")

    def _go_to_profile(self, driver):
        """Переход в личный кабинет"""
        driver.find_element(*MainPage.mn_profile_button).click()
        self._wait_for_element(driver, Navigatorprofile.np_info_message)

    def _check_profile_page(self, driver):
        """Проверка, что открыта страница профиля"""
        profile = self._wait_for_element(driver, Navigatorprofile.np_history_shop_button)
        assert driver.current_url == Urls.url_profile, f"Ожидался URL {Urls.url_profile}, но получен {driver.current_url}"
        assert profile.text == 'История заказов', f"Ожидался текст 'История заказов', но получен {profile.text}"

    def _check_constructor_page(self, driver):
        """Проверка, что открыта страница конструктора"""
        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0, "Заголовок 'Соберите бургер' не найден"
        assert h1_tag[0].text == 'Соберите бургер', f"Ожидался текст 'Соберите бургер', но получен {h1_tag[0].text}"

    def test_click_profile_button_open_profile_form(self, login):
        """Открыть личный кабинет"""
        driver = login
        self._go_to_profile(driver)
        self._check_profile_page(driver)
        driver.quit()

    def test_click_constructor_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор'"""
        driver = login
        self._go_to_profile(driver)
        driver.find_element(*MainPage.mn_constructor_button).click()
        self._check_constructor_page(driver)
        driver.quit()

    def test_click_logo_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии на лого"""
        driver = login
        self._go_to_profile(driver)
        driver.find_element(*MainPage.mn_logo).click()
        self._check_constructor_page(driver)
        driver.quit()

    def test_click_logout_button_in_lk_open_login_form(self, login):
        """Выход из аккаунта"""
        driver = login
        self._go_to_profile(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Navigatorprofile.np_logout_button)).click()
        self._wait_for_element(driver, AuthLogin.al_login_button_any_forms)
        assert driver.current_url == Urls.url_login
        login_button = self._wait_for_element(driver, AuthLogin.al_element_with_login_text)
        assert login_button.text == 'Вход'
        driver.quit()