from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_good_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET_LOCATOR), "Basket is empty"

    def should_be_text_your_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_LOCATOR), "Basket is not empty"