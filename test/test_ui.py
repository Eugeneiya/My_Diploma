import pytest
from selenium import webdriver
from UI_test_pages.UI_address_page import Address
from UI_test_pages.UI_search_page import Search
from UI_test_pages.UI_order_page import Order
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.maximize_window()

    yield driver

    driver.quit()


@allure.title("Тестирование формы ввода адреса доставки")
@allure.description("Тест проверяет корректность работы "
                "формы адреса доставки")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.CRITICAL)
def test_address(driver):
    """Тест проверяет ввод адреса доставки"""
    with allure.step("Открытие сайта 'Деливери'"):
        UI_address_page = Address(driver)
        UI_address_page.driver_open()
    with allure.step("Открытие формы ввода адреса доставки"):
        UI_address_page.address_form_open()
    with allure.step("Заполнение формы ввода адреса доставки"):
        UI_address_page.address_form_fill()
        
@allure.title("Позитивная проверка поиска товара с названием на английском")
@allure.description("Тест проверяет корректность поиска "
                "товара с названием на английском")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.BLOCKER)
def test_eng_search_positive(driver):
    """Тест проверяет поиск товаров с английским названием"""
    with allure.step("Поиск товара с названием на английском"):
        UI_search_page = Search(driver)
        UI_search_page.driver_open()
        UI_search_page.eng_goods_name_search()


@allure.title("Позитивная проверка поиска компании с "
                "названием на русском и пробелами")
@allure.description("Тест проверяет корректность поиска "
                    "компании с названием на русском и пробелами")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.BLOCKER)
def test_rus_search_positive(driver):
    """Тест проверяет поиск компании с названием на русском и пробелами"""
    with allure.step("Поиск компании с названием на русском и пробелами"):
        UI_search_page = Search(driver)
        UI_search_page.driver_open()
        UI_search_page.rus_entity_name_search()


@allure.title("Негативная проверка поиска по 2 пробелам в строке поиска")
@allure.description("Тест проверяет корректность работы сайта "
                    "при отправке 2 пробелов в строке поиска")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.NORMAL)
def test_whitespaces_search_negative(driver):
    """Негативная проверка поиска по 2 пробелам в строке поиска"""
    with allure.step("Поиск по 2 пробелам в строке поиска"):
        UI_search_page = Search(driver)
        UI_search_page.driver_open()
        UI_search_page.two_whitespaces_search()


@allure.title("Негативная проверка при отправке пустого запроса при поиске")
@allure.description("Тест проверяет корректность работы сайта "
                    "при отправке пустого запроса в строке поиска")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.NORMAL)
def test_null_search_negative(driver):
    """Негативная проверка отправки пустого запроса в строке поиска"""
    with allure.step("Поиск при отправке пустого запроса"):
        UI_search_page = Search(driver)
        UI_search_page.driver_open()
        UI_search_page.null_search()


@allure.title("Тестирование добавления товара в заказ")
@allure.description("Тест проверяет корректность работы сайта "
                    "при заказе товаров с указанием адреса доставки")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.BLOCKER)
def test_order(driver):
    """Тест проверяет добавление товаров в корзину для заказа"""
    with allure.step("Открытие сайта 'Деливери'"):
        UI_order_page = Order(driver)
        UI_order_page.driver_open()
    with allure.step("Ввод адреса доставки"):
        UI_order_page.address()
    with allure.step("Поиск товара на сайте"):
        UI_order_page.goods_search()
    with allure.step("Добавление товара в корзину"):
        UI_order_page.goods_add()
    