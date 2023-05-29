from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")


class ProductPageLocators:
    TITLE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_WITH_NAME_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    TITLE_WITH_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_WITH_PRICE_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")