from .base_page import BasePage


class HomePage(BasePage):
    DEST_INPUT = 'input[id="bigsearch-query-location-input"]'
    DATE_BUTTON = 'button[data-state--date-string="{date_str}"]'
    GUESTS_BUTTON = 'div[data-testid="structured-search-input-field-guests-button"]'
    ADULTS_BUTTON = 'button[data-testid="stepper-adults-increase-button"]'
    CHILD_BUTTON = 'button[data-testid="stepper-children-increase-button"]'
    SEARCH_BUTTON = 'button[data-testid="structured-search-input-search-button"]'
    FIRST_SEARCH_OPTION = 'div[data-testid="option-0"]'

    def search(self, destination: str):
        self.goto('/')
        self.fill(self.DEST_INPUT, destination)
        self.page.wait_for_selector(self.FIRST_SEARCH_OPTION, timeout=5000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

    def select_date(self, date_str: str):
        self.click(self.DATE_BUTTON.format(date_str=date_str))

    def select_guests(self, adults: int = 2, children: int = 0):
        self.click(self.GUESTS_BUTTON)
        for _ in range(adults):
            self.click(self.ADULTS_BUTTON)
        for _ in range(children):
            self.click(self.CHILD_BUTTON)

    def submit_search(self):
        self.click(self.SEARCH_BUTTON)
