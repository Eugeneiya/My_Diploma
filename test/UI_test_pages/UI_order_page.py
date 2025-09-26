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

    @allure.step("Авторизация по логину и паролю")
    def auth(self):
        """Выполняет авторизацию на сайте для заказа"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                        "//span[@class='DesktopUIButton_content']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//div[@class='Header']")))
        self.driver.find_element(By.XPATH,
                         "//a[@id='passp:exp-register']").click()
        self.driver.find_element(By.XPATH,
                        "//button[contains(text(),'Войти по логину')]").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                         ".passp-add-account-page-title")))
        self.driver.find_element(By.CSS_SELECTOR,
                    "#passp-field-login").send_keys("eugeneiyab@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR,
                    "button[id='passp:sign-in']").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                    ".WelcomePage-tagline")))
        self.driver.find_element(By.CSS_SELECTOR,
                        "#passp-field-passwd").send_keys("SkyPro2025")
        self.driver.find_element(By.CSS_SELECTOR,
                            "button[id='passp:sign-in']").click()

    @allure.step("Выбор адреса доставки")
    def location_setup(self):
        """Устанавливает адрес доставки"""
        with allure.step("Нажатие на строку с адресом доставки"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                ".r1jyb6b1.s1v4x2t8.vjiwpdh.syv67cr.bzqs12k.alrmgpb.b1b9rjk2"))
                ).click()
        with allure.step("Нажатие на кнопку 'Дом'"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                ".UiKitSlotCore_control"))).click()
                
    @allure.step("Поиск товара на сайте")
    def goods_search(self):
        """Осуществляет поиск и добавление товара в корзину"""
        search = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#id_1")))
        search.send_keys("Морковь мытая")
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Найти')]").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='c15qgkvo']")))

    @allure.step("Добавление товара в корзину")
    def goods_add(self):
        """Осуществляет добавление товара в корзину"""
        with allure.step("Нажатие на запрошенный товар"):
            goods = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button[aria-label='Морковь мытая 1 кг, 110, 1кг']"))
                )
            goods.click()
        with allure.step("Нажатие на кнопку 'Добавить'"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                    ".r1jyb6b1.slw94yn.v102ekr4.syv67cr.cnts9l4"))).click()
        with allure.step("Нажатие на кнопку 'Оформить заказ'"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                ".r1jyb6b1.slw94yn.v102ekr4.syv67cr.cnts9l4.ftcyuun"))).click()

    @allure.step("Проверка наличия добавленного товара в заказе")
    def order_check(self):
        """Выполняет проверку наличия добавленного товара в заказе"""
        with allure.step("Проверка отображения товара в заказе"):
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH,
            "//h3[contains(text(),'Морковь мытая 1 кг')]")))
            assert element.is_displayed()
        with allure.step("Закрытие сайта 'Деливери"):
            self.driver.quit()
