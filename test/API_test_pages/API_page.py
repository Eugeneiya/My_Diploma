import requests
import allure


class API:
    def __init__(self, url):
        self.url = url
        self.headers = {"Content-Type": "application/json"}

    @allure.step("Поиск товара по названию '{text}' и локации")
    def search_eats(self, text, location):
        eats = {
            "text": text,
            "location": location
        }
        resp = requests.post(self.url + 'eats/v1/full-text-search/v1/search',
                             json=eats, headers=self.headers)
        return resp.status_code

    @allure.step("Поиск товара невалидным методом")
    def search_eats_invalid_method(self, text, location):
        eats = {
            "text": text,
            "location": location
        }
        resp = requests.get(self.url + 'eats/v1/full-text-search/v1/search',
                             json=eats, headers=self.headers)
        return resp.status_code
