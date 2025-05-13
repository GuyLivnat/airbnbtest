import time
from typing import List, Tuple
from playwright.sync_api import Locator
from .base_page import BasePage


class SearchResultsPage(BasePage):
    CARD = 'div[data-testid="card-container"]'
    PRICE = 'div[data-testid="price-availability-row"]'
    TITLE = 'div[data-testid="listing-card-title"]'
    NAME = 'span[data-testid="listing-card-name"]'
    NEXT_BUTTON = 'a[aria-label="Next"]'
    SEARCH_DATE = 'button[data-testid="little-search-anytime"]'
    SEARCH_LOCATION = 'button[data-testid="little-search-location"]'
    SEARCH_COUNT = 'button[data-testid="little-search-guests"]'


    def wait_for_listings(self, timeout: int = 10000):
        # ensure at least one card appears
        self.page.wait_for_selector(self.CARD, timeout=timeout)

    def get_all_listings(self) -> List[Locator]:
        self.wait_for_listings()
        return self.locator(self.CARD).all()

    def click_next_page(self) -> bool:
        next_btn = self.page.query_selector(self.NEXT_BUTTON)

        if not next_btn:
            return False

        next_btn.click()
        self.wait_for_listings()
        return True

    @staticmethod
    def get_rating(card: Locator) -> float:
        deepest = card.locator("xpath=./div[last()]/div[last()]/div[last()]")  # Why did they hide this with no ID?
        spans = deepest.locator("span")

        if spans.count() == 0:  # no <span> means no rating
            return 0.0
        text = deepest.locator("span").first.inner_text()
        if "new" in text.lower():
            return 0.0
        return float(text[:2])

    def get_price(self, card: Locator) -> int:
        text = (card.locator(f"{self.PRICE} button span").first.inner_text())
        for string in ['\u20aa', ' ', ',', 'total']:  # \u20aa is the NIS sign
            text = text.replace(string, '')
        return int(text)

    def get_title(self, card: Locator) -> str:
        return card.locator(self.TITLE).inner_text().strip()

    def get_name(self, card: Locator) -> str:
        return card.locator(self.NAME).inner_text().strip()

    def get_current_search_settings(self) -> Tuple[str, str, str]:
        self.wait_for_search_parameters(f"{self.SEARCH_LOCATION} div")
        location = (self.locator(f"{self.SEARCH_LOCATION} div").inner_text())
        date = (self.locator(f"{self.SEARCH_DATE} div").inner_text())
        guest_count = (self.locator(f"{self.SEARCH_COUNT} div").first.inner_text())
        return location, date, guest_count

    def wait_for_search_parameters(self, selector: str, timeout: int = 3, poll_interval: float = 0.1) -> None:
        end_time = time.time() + timeout

        while time.time() < end_time:
            text = self.get_text(selector)
            if text:
                return
            time.sleep(poll_interval)

        raise TimeoutError

