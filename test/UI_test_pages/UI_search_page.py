from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Search:
    def __init__(self, driver):
        """Конструктор класса Search"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Ввод в поисковую строку названия товара "
               "на английском и нажатие на кнопку 'Найти'")
    def eng_goods_name_search(self):
        """Проверяет поиск товара с названием на английском"""
        with allure.step("Ввод в поисковую строку названия "
                         "товара на английском"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                         "#id_1"))).send_keys("milk")
        with allure.step("Нажатие на кнопку 'Найти'"):
            self.driver.find_element(By.XPATH,
                          "//span[contains(text(),'Найти')]").click()
        with allure.step("Проверка результата поиска"):
            self.wait.until(
                  EC.visibility_of_element_located((By.XPATH,
                    "//*[contains(., 'Найдено') or contains(., 'Найден')]")))
            self.wait.until(
                  EC.visibility_of_element_located((By.XPATH,
                              "//div[@class='c15qgkvo']")))
            elements = self.driver.find_elements(By.XPATH,
                "//*[contains(text(), 'milk') or contains(text(), 'молоко')]")
            assert len(elements) > 0
        with allure.step("Закрытие сайта 'Деливери'"):
            self.driver.quit()

    @allure.step("Открытие сайта 'Деливери'")
    def driver_open(self):
        """Открывает сайт 'Деливери'"""
        self.driver.get("https://market-delivery.yandex.ru")

    @allure.step("Ввод в поисковую строку названия компании на "
               "русском с пробелами и нажатие на кнопку 'Найти'")
    def rus_entity_name_search(self):
        """Проверяет поиск кафе/ресторана с названием на русском и пробелами"""
        with allure.step("Ввод в поисковую строку названия компании на русском"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                         "#id_1"))).send_keys("Яндекс Лавка")
        with allure.step("Нажатие на кнопку 'Найти'"):
            self.driver.find_element(By.XPATH,
                         "//span[contains(text(),'Найти')]").click()
        with allure.step("Проверка результата поиска"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH,
                    "//*[contains(., 'Найдено') or contains(., 'Найден')]")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH,
                              "//div[@class='c15qgkvo']")))
            elements = self.driver.find_elements(By.XPATH,
                         "//*[contains(text(), 'Яндекс Лавка')]")
            assert len(elements) > 0
        with allure.step("Закрытие сайта 'Деливери'"):
            self.driver.quit()

    @allure.step("Открытие сайта 'Деливери'")
    def driver_open(self):
        """Открывает сайт 'Деливери'"""
        self.driver.get("https://market-delivery.yandex.ru")

    @allure.step("Ввод в поисковую строку 2 пробелов "
    "и нажатие на кнопку 'Найти'")
    def two_whitespaces_search(self):
        """Проверяет поиск по 2 пробелам в строке поиска"""
        with allure.step("Ввод в поисковую строку 2 пробелов"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                         "#id_1"))).send_keys("  ")
        with allure.step("Нажатие на кнопку 'Найти'"):
            self.driver.find_element(By.XPATH,
                         "//span[contains(text(),'Найти')]").click()
        with allure.step("Проверка результата поиска"):
            results_header = self.wait.until(
                  EC.visibility_of_element_located((By.XPATH,
                         "//h2[contains(text(),'Часто ищут')]")))
            assert results_header.is_displayed()
        with allure.step("Закрытие сайта 'Деливери'"):
            self.driver.quit()

    @allure.step("Открытие сайта 'Деливери'")
    def driver_open(self):
        """Открывает сайт 'Деливери'"""
        self.driver.get("https://market-delivery.yandex.ru")

    @allure.step("Оставление поисковой строки пустой и "
                    "нажатие на кнопку 'Найти'")
    def null_search(self):
        """Проверяет результат отправки пустого запроса в строке поиска"""
        with allure.step("Отправка пустого запроса"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                          "#id_1"))).send_keys("  ")
            self.driver.find_element(By.XPATH,
                          "//span[contains(text(),'Найти')]").click()
        with allure.step("Проверка результата поиска"):
            results_header = self.wait.until(
                  EC.visibility_of_element_located((By.XPATH,
                         "//h2[contains(text(),'Часто ищут')]")))
        assert results_header.is_displayed()
        with allure.step("Закрытие сайта 'Деливери'"):
            self.driver.quit()
