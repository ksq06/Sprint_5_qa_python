from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *

class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        """Проверка перехода на 'Соусы'"""
        driver = login
        self._go_to_constructor(driver)
        self._click_sauces_button(driver)
        h_sauce = self._wait_for_element(driver, MainPage.mn_h_sauces)
        assert h_sauce.text == 'Соусы'
        driver.quit()

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        """Проверка перехода на 'Начинки'"""
        driver = login
        self._go_to_constructor(driver)
        self._click_filling_button(driver)
        h_filling = self._wait_for_element(driver, MainPage.mn_h_filling)
        assert h_filling.text == 'Начинки'
        driver.quit()

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Проверка перехода на 'Булки'"""
        driver = login
        self._go_to_constructor(driver)
        self._click_filling_button(driver)
        self._click_bun_button(driver)
        h_bun = self._wait_for_element(driver, MainPage.mn_h_bun)
        assert h_bun.text == 'Булки'
        driver.quit()

    def _go_to_constructor(self, driver):
        """Переход в конструктор"""
        driver.find_element(*MainPage.mn_constructor_button).click()

    def _click_sauces_button(self, driver):
        """Клик на кнопку 'Соусы'"""
        driver.find_element(*MainPage.mn_sauces_button).click()

    def _click_filling_button(self, driver):
        """Клик на кнопку 'Начинки'"""
        driver.find_element(*MainPage.mn_filling_button).click()

    def _click_bun_button(self, driver):
        """Клик на кнопку 'Булки'"""
        driver.find_element(*MainPage.mn_bun_button).click()

    def _wait_for_element(self, driver, locator, timeout=10):
        """Ожидание появления элемента на странице"""
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )