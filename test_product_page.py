from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_correct_book_name_in_cart()
    page.should_be_correct_book_price_in_cart()

