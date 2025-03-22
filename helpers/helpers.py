from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *
from selenium.common.exceptions import TimeoutException
from web_locators.locators import AuthLogin, MainPage
from data.data import PersonData
from data.urls import Urls
from selenium.webdriver.common.by import By

def go_to_constructor(driver):
    """Переход в конструктор"""
    driver.find_element(*MainPage.mn_constructor_button).click()

def click_sauces_button(driver):
    """Клик на кнопку 'Соусы'"""
    driver.find_element(*MainPage.mn_sauces_button).click()

def click_filling_button(driver):
    """Клик на кнопку 'Начинки'"""
    driver.find_element(*MainPage.mn_filling_button).click()

def click_bun_button(driver):
    """Клик на кнопку 'Булки'"""
    driver.find_element(*MainPage.mn_bun_button).click()

def wait_for_element_construction(driver, locator, timeout=10, attribute=None, initial_value=None):
    """Ожидание появления элемента на странице"""
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

    if attribute and initial_value is not None:
        WebDriverWait(driver, timeout).until(
            lambda d: element.get_attribute(attribute) != initial_value
        )

    return element

def wait_for_element_login(driver, locator, timeout=10):
    """Ожидание появления элемента на странице"""
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        raise TimeoutException(f"Элемент {locator} не найден на странице")

def login(driver):
    """Авторизация пользователя"""
    driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
    driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)
    driver.find_element(*AuthLogin.al_login_button_any_forms).click()

def check_main_page(driver):
    """Проверка, что пользователь на главной странице"""
    order_button = wait_for_element_login(driver, MainPage.mn_order_button)
    assert driver.current_url == Urls.url_main_page
    assert order_button.text == 'Оформить заказ'

def wait_for_element_navigator(driver, locator, timeout=10):
    """Ожидание появления элемента на странице"""
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        raise TimeoutException(f"Элемент {locator} не найден на странице")

def go_to_profile(driver):
    """Переход в личный кабинет"""
    driver.find_element(*MainPage.mn_profile_button).click()
    wait_for_element_navigator(driver, Navigatorprofile.np_info_message)

def check_profile_page(driver):
    """Проверка, что открыта страница профиля"""
    profile = wait_for_element_navigator(driver, Navigatorprofile.np_history_shop_button)
    assert driver.current_url == Urls.url_profile, f"Ожидался URL {Urls.url_profile}, но получен {driver.current_url}"
    assert profile.text == 'История заказов', f"Ожидался текст 'История заказов', но получен {profile.text}"

def check_constructor_page(driver):
    """Проверка, что открыта страница конструктора"""
    h1_tag = driver.find_elements(*Navigatorprofile.H1_TAG)
    assert len(h1_tag) > 0, "Заголовок 'Соберите бургер' не найден"
    assert h1_tag[0].text == 'Соберите бургер', f"Ожидался текст 'Соберите бургер', но получен {h1_tag[0].text}"

def go_to_registration_page(driver):
    """Переход на страницу регистрации"""
    driver.get(Urls.url_register)

def fill_registration_form(driver, name, email, password):
    """Заполнение формы регистрации"""
    driver.find_element(*AuthRegister.ar_name_field).send_keys(name)
    driver.find_element(*AuthRegister.ar_email_field).send_keys(email)
    driver.find_element(*AuthRegister.ar_password_field).send_keys(password)

def submit_registration_form(driver):
    """Нажатие кнопки 'Зарегистрироваться'"""
    driver.find_element(*AuthRegister.ar_register_button).click()

def wait_for_element_registration(driver, locator, timeout=10):
    """Ожидание появления элемента на странице"""
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        raise TimeoutException(f"Элемент {locator} не найден на странице")