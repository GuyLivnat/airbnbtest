from base_page import BasePage


class HomePage(BasePage):
    DEST_INPUT = 'input[id^="bigsearch-query-detached-query-input"]'
    CHECKIN_INPUT = 'input[name="checkin"]'
    CHECKOUT_INPUT = 'input[name="checkout"]'
    ADULTS_BUTTON = 'button[data-testid="stepper-adults-increase-button"]'
    CHILD_BUTTON = 'button[data-testid="stepper-children-increase-button"]'
    SEARCH_BUTTON = 'button[type="submit"]'

    def search(self, destination: str, checkin: str, checkout: str, adults: int, children: int):
        self.goto('/')
        self.fill(self.DEST_INPUT, destination)
        self.fill(self.CHECKIN_INPUT, checkin)
        self.fill(self.CHECKOUT_INPUT, checkout)
        for _ in range(adults - 1):  # website starts with 1 adult
            self.click(self.ADULTS_BUTTON)
        for _ in range(children):
            self.click(self.CHILD_BUTTON)
        self.click(self.SEARCH_BUTTON)