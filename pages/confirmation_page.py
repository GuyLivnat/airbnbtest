from .base_page import BasePage


class ConfirmationPage(BasePage):
    DATE = 'div[data-section-id="DATE_PICKER"]'
    GUEST_COUNT = 'div[data-plugin-in-point-id="GUEST_PICKER"]'
    COUNTRY = 'select[data-testid="login-signup-countrycode"]'
    PHONE_NUM = 'input[data-testid="login-signup-phonenumber"]'

    def get_guest_count(self):
        return self.locator(f"{self.GUEST_COUNT} div").nth(5).inner_text()

    def get_dates(self):
        return self.locator(f"{self.DATE} div").nth(3).inner_text()

    def choose_country(self, country: str):
        inp = self.locator(self.COUNTRY)
        inp.select_option(country)

    def input_phone_number(self, number: int):
        inp = self.locator(self.PHONE_NUM)
        inp.fill(str(number))

