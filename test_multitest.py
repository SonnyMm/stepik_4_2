import pytest
from selenium import webdriver
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()

    # Добавляем товар в корзину
    product_page.add_to_basket()

    # Решаем задачу и получаем код
    product_page.solve_quiz_and_get_code()

    # Получаем название товара и цену с страницы товара
    product_name = product_page.get_product_name()
    basket_price = product_page.get_basket_price()

    # Получаем сообщение о добавлении товара в корзину
    success_message = product_page.get_success_message()

    # Извлекаем название товара и цену из сообщения о добавлении товара в корзину
    extracted_product_name = product_page.extract_product_name_from_message(success_message)
    extracted_basket_price = product_page.extract_basket_price_from_message(success_message)

    # Проверяем, что название товара в сообщении совпадает с названием товара на странице
    assert product_name == extracted_product_name, f"Expected product name '{product_name}', but got '{extracted_product_name}'"

    # Проверяем, что цена товара в корзине совпадает с ценой товара на странице
    assert basket_price == extracted_basket_price, f"Expected basket price '{basket_price}', but got '{extracted_basket_price}'"

@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", marks=pytest.mark.xfail),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", marks=pytest.mark.xfail),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", marks=pytest.mark.xfail),
    # добавьте другие ссылки, где обнаружен баг
])
def test_guest_can_add_product_to_basket_with_xfail(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()

    # Добавляем товар в корзину
    product_page.add_to_basket()

    # Решаем задачу и получаем код
    product_page.solve_quiz_and_get_code()

    # Получаем название товара и цену с страницы товара
    product_name = product_page.get_product_name()
    basket_price = product_page.get_basket_price()

    # Получаем сообщение о добавлении товара в корзину
    success_message = product_page.get_success_message()

    # Извлекаем название товара и цену из сообщения о добавлении товара в корзину
    extracted_product_name = product_page.extract_product_name_from_message(success_message)
    extracted_basket_price = product_page.extract_basket_price_from_message(success_message)

    # Проверяем, что название товара в сообщении совпадает с названием товара на странице
    assert product_name == extracted_product_name, f"Expected product name '{product_name}', but got '{extracted_product_name}'"

    # Проверяем, что цена товара в корзине совпадает с ценой товара на странице
    assert basket_price == extracted_basket_price, f"Expected basket price '{basket_price}', but got '{extracted_basket_price}'"
pytest -s test_product_page.py
