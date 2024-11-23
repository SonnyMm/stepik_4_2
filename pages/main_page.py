from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

        # Обрабатываем alert, если он появляется
        try:
            alert = self.browser.switch_to.alert
            alert.accept()  # принимаем alert
        except:
            pass  # Если alert не появился, просто продолжаем выполнение
