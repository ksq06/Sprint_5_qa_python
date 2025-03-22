from helpers.helpers import go_to_constructor, click_sauces_button, click_filling_button, click_bun_button, wait_for_element_construction

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *

class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        """Проверка перехода на 'Соусы' с учетом изменения класса"""
        driver = login
        go_to_constructor(driver)

        sauces_tab = wait_for_element_construction(driver, MainPage.mn_sauces_button)
        old_class = sauces_tab.get_attribute("class")

        click_sauces_button(driver)

        WebDriverWait(driver, 5).until(
            lambda d: sauces_tab.get_attribute("class") != old_class
        )

        new_class = sauces_tab.get_attribute("class")
        assert new_class != old_class, "Таб 'Соусы' не стал активным"

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        """Проверка перехода на 'Начинки' с учетом изменения класса"""
        driver = login
        go_to_constructor(driver)

        filling_tab = wait_for_element_construction(driver, MainPage.mn_filling_button)
        old_class = filling_tab.get_attribute("class")

        click_filling_button(driver)

        WebDriverWait(driver, 5).until(
            lambda d: filling_tab.get_attribute("class") != old_class
        )

        new_class = filling_tab.get_attribute("class")
        assert new_class != old_class, "Таб 'Начинки' не стал активным"

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Проверка перехода на 'Булки' с учетом изменения класса"""
        driver = login
        go_to_constructor(driver)
        click_filling_button(driver)

        bun_tab = wait_for_element_construction(driver, MainPage.mn_bun_button)
        old_class = bun_tab.get_attribute("class")

        click_bun_button(driver)

        bun_tab = wait_for_element_construction(driver, MainPage.mn_bun_button)  # Повторно находим элемент

        WebDriverWait(driver, 5).until(
            lambda d: bun_tab.get_attribute("class") != old_class
        )

        new_class = bun_tab.get_attribute("class")
        assert new_class != old_class, "Таб 'Булки' не переключился"