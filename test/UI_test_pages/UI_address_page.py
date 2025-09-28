from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Address:
    def __init__(self, driver):
        """Конструктор класса Address"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открытие сайта 'Деливери'")
    def driver_open(self):
        """Открывает сайт 'Деливери'"""
        self.driver.get("https://market-delivery.yandex.ru")

    @allure.step("Открытие окна ввода адреса доставки")
    def address_form_open(self):
        """Нажимает кнопку с адресом доставки, открывает окно 'Укажите адрес доставки'"""
        with allure.step("Нажатие на строку с текущим адресом доставки"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
            ".r1jyb6b1.s1v4x2t8.vjiwpdh.syv67cr.bzqs12k.alrmgpb.b1b9rjk2"))).click()
        with allure.step("Нажатие на строку 'Куда доставить?', открытие "
            "окна 'Укажите адрес доставки'"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                ".UiKitSuperViewButton_root"))).click()

    @allure.step("Заполнение формы ввода адреса доставки")
    def address_form_fill(self):
        """Заполняет форму ввода адреса доставки',
        нажимает на кнопку 'ОК'"""
        with allure.step("Очистка адресной строки"):
            my_address = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                        "input[placeholder='Введите улицу и дом']")))
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                        ".mvl7tin.UiKitImgIcon.r1mbrood.c1stz5ga.UiKitImgIcon"))).click()
        with allure.step("Ввод адреса в адресную строку"):
            my_address.send_keys("Проспект Вернадского, 10, Москва")
        with allure.step("Выбор адреса по КЛАДР из выпадающего списка"):
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                "li[id='react-autowhatever-1--item-0'] div[class='UiKitSlotCore_control']"))).click()
        with allure.step("Нажатие на кноку 'ОК'"):    
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                        ".r1jyb6b1.s1v4x2t8.v102ekr4.syv67cr.o16sqpc5"))).click()
        with allure.step("Проверка адреса на главной странице"):
            self.wait.until(
                  EC.visibility_of_element_located((By.XPATH,
                    "//*[contains(., 'проспект Вернадского, 10')]")))


