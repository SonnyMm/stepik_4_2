import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get("https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer6")
    yield browser
    browser.quit()

def test_add_to_basket(browser):
    # Находим и нажимаем на кнопку "Add to basket"
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    add_to_basket_button.click()
    
    # Даем время на выполнение асинхронных действий (например, появления сообщения)
    time.sleep(1)
    
    # Проверяем, что сообщение о добавлении товара в корзину появилось
    messages = browser.find_elements(By.CSS_SELECTOR, "#messages .alert-success")
    
    # Ищем сообщение о добавлении товара в корзину и извлекаем название товара
    product_name = browser.find_element(By.CSS_SELECTOR, "#messages .alert-success .alertinner strong").text
    assert "Coders at Work" in product_name, f"Product name '{product_name}' not found in alert"
    
    # Проверяем, что сообщение содержит цену
    price_message = browser.find_element(By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong").text
    assert "£19.99" in price_message, f"Price '{price_message}' not found in alert"
