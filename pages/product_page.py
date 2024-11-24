# product_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")

    def add_to_basket(self):
        button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        """Получаем название товара с страницы товара."""
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_basket_price(self):
        """Получаем цену товара с корзины."""
        return self.browser.find_element(*self.BASKET_PRICE).text

    def get_success_message(self):
        """Получаем сообщение о добавлении товара в корзину."""
        return self.browser.find_element(*self.SUCCESS_MESSAGE).text

    def extract_product_name_from_message(self, success_message):
        """Извлекаем название товара из сообщения о добавлении в корзину."""
        # Предполагаем, что название товара присутствует в success_message
        return success_message.split(":")[1].strip()

    def extract_basket_price_from_message(self, success_message):
        """Извлекаем цену товара из сообщения о добавлении в корзину."""
        # Предполагаем, что цена товара также присутствует в success_message
        return success_message.split("is")[1].strip()
