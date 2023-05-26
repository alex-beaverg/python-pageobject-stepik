from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_WITH_NAME_OF_ADDED_PRODUCT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_WITH_NAME_OF_ADDED_PRODUCT), \
            "Success message is not disappeared, but should disappear"

    def add_product_to_basket(self):
        add_product_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_product_btn.click()

    def should_be_correct_product_name_in_message(self):
        product_name_in_title = self.browser.find_element(*ProductPageLocators.TITLE_WITH_PRODUCT_NAME).text
        product_name_in_message = self.browser\
            .find_element(*ProductPageLocators.MESSAGE_WITH_NAME_OF_ADDED_PRODUCT).text
        assert product_name_in_title == product_name_in_message, \
            "Product name in title is not equal product name in message"

    def should_be_correct_product_price_in_message(self):
        product_price_in_title = self.browser.find_element(*ProductPageLocators.TITLE_WITH_PRODUCT_PRICE).text
        product_price_in_message = self.browser\
            .find_element(*ProductPageLocators.MESSAGE_WITH_PRICE_OF_ADDED_PRODUCT).text
        assert product_price_in_title == product_price_in_message, \
            "Product price in title is not equal product name in message"