from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), (
            "Basket items are presented, but should not be"
        )

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), (
            "Message about empty basket is not presented"
        )