from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Order:
    def __init__(self, driver):
        """Конструктор класса Order"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Открытие сайта 'Деливери'")
    def driver_open(self):
        """Открывает сайт 'Деливери'"""
        self.driver.get("https://market-delivery.yandex.ru")

    @allure.step("Ввод адреса доставки")
    def address(self):
        """Выполняет ввод адреса доставки заказа"""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            ".r1jyb6b1.s1v4x2t8.vjiwpdh.syv67cr.bzqs12k.alrmgpb.b1b9rjk2"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                        ".UiKitSuperViewButton_root"))).click()
        my_address = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Введите улицу и дом']")))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            ".mvl7tin.UiKitImgIcon.r1mbrood.c1stz5ga.UiKitImgIcon"))).click()
        my_address.send_keys("Проспект Вернадского, 10, Москва")
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
            "li[id='react-autowhatever-1--item-0'] div[class='UiKitSlotCore_control']"))
                ).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                ".r1jyb6b1.s1v4x2t8.v102ekr4.syv67cr.o16sqpc5"))).click()

    @allure.step("Поиск товара на сайте")
    def goods_search(self):
        """Осуществляет поиск товара"""
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                            "#id_1")))
        search.send_keys("морковь весовая")
        self.driver.find_element(By.XPATH,
                            "//span[contains(text(),'Найти')]").click()
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH,
                        "//div[@class='c15qgkvo']"))
            )

    @allure.step("Добавление запрошенного товара в корзину")
    def goods_add(self):
        """Осуществляет добавление запрошенного товара в корзину"""
        with allure.step("Нажатие на запрошенный товар (в маг. 'Пятерочка')"):
            self.wait.until(EC.element_to_be_clickable((By.XPATH,
            "(//button[@aria-label='Морковь весовая , 12, 500г'])[1]"))).click()
        with allure.step("Нажатие на кнопку 'Добавить'"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                    ".r1jyb6b1.slw94yn.v102ekr4.syv67cr.cnts9l4"))).click()
        with allure.step("Нажатие на кнопку 'Оформить заказ'"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                ".r1jyb6b1.slw94yn.v102ekr4.syv67cr.cnts9l4.ftcyuun"))).click()
