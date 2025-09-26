from API_test_pages.API_page import API
import allure


api = API('https://market-delivery.yandex.ru/')
my_headers = {"Content-Type": "application/json"}


@allure.title("Позитивная проверка поиска товаров на сайте")
@allure.description("Тест проверяет корректность поиска "
                "на сайте по названию товаров и локации")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.CRITICAL)
def test_API_search():
    resp = api.search_eats(
        "Бабагануш", {"longitude": 37.397072, "latitude": 55.868092}
        )
    assert resp == 200


@allure.title("Негативная проверка поиска товаров по 1 символу")
@allure.description("Тест проверяет корректность статус-кода "
                    "при поиске по 1 символу")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.NORMAL)
def test_1_symbol_search():
    resp = api.search_eats(
        "О", {"longitude": 37.397072, "latitude": 55.868092}
        )
    assert resp == 400


@allure.title("Негативная проверка при пустом запросе в строке поиска")
@allure.description("Тест проверяет корректность статус-кода "
                    "при пустом запросе в строке поиска")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.NORMAL)
def test_empty_search():
    resp = api.search_eats(
        "", {"longitude": 37.397072, "latitude": 55.868092}
        )
    assert resp == 200


@allure.title("Негативная проверка при неправильном методе для поиска")
@allure.description("Тест проверяет корректность статус-кода "
                    "при неправильном методе для поиска")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.MINOR)
def test_invalid_method():
    resp = api.search_eats_invalid_method(
        "Пицца", {"longitude": 37.397072, "latitude": 55.868092}
        )
    assert resp == 400


@allure.title("Негативная проверка поиска при отсутствии данных о локации")
@allure.description("Тест проверяет корректность статус-кода "
                    "при поиске без данных о локации")
@allure.feature("Сайт доставки еды и продуктов 'Деливери'")
@allure.severity(allure.severity_level.MINOR)
def test_empty_location():
    resp = api.search_eats("Пицца", {"longitude": "", "latitude": ""})
    assert resp == 400
