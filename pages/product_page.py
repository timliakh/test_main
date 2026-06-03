from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_be_product_name_in_message(self, product_name):
        message_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE
        ).text
        assert product_name == message_name, (
            f"Product name '{product_name}' does not match message name "
            f"'{message_name}'"
        )

    def should_be_product_price(self, product_price):
        assert self.get_product_price() == product_price, (
            "Product price on page does not match"
        )

    def add_product_to_basket(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_product_name_in_message(product_name)
        self.should_be_product_price(product_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"