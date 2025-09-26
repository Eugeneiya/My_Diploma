from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Authorization:
    def __init__(self, driver):
        """Конструктор класса Authorization"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открытие сайта 'Деливери'")
    def driver_open(self):
        """Открывает сайт 'Деливери'"""
        self.driver.get("https://market-delivery.yandex.ru")

    @allure.step("Открытие формы авторизации")
    def auth_page_open(self):
        """Нажимает кнопку 'Войти', открывает окно авторизации"""
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                        "//span[@class='DesktopUIButton_content']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                "//div[@class='Header']")))

    @allure.step("Переход в форму авторизации по логину")
    def login_form(self):
        """Переводит в окно авторизации по логину,
        нажимает на кнопку 'Продолжить'"""
        self.driver.find_element(By.XPATH,
                        "//a[@id='passp:exp-register']").click()
        self.driver.find_element(By.XPATH,
                        "//button[contains(text(),'Войти по логину')]").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                        ".passp-add-account-page-title")))

    @allure.step("Заполнение окна авторизации по логину,"
                " нажатие на 'Продолжить'")
    def login_form_fill(self):
        """Вводит логин, пароль, нажимает на кнопку 'Продолжить'"""
        self.driver.find_element(By.CSS_SELECTOR,
                    "#passp-field-login").send_keys("eugeneiyab@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR,
                    "button[id='passp:sign-in']").click()
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                    ".WelcomePage-tagline")))
        self.driver.find_element(
            By.CSS_SELECTOR, "#passp-field-passwd").send_keys("SkyPro2025")
        self.driver.find_element(By.CSS_SELECTOR,
                    "button[id='passp:sign-in']").click()
