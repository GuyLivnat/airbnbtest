from typing import List
from playwright.sync_api import Locator
from .base_page import BasePage


class SearchResultsPage(BasePage):
    FILTER_DEST = 'button[aria-label*="location"]'
    FILTER_DATES = 'button[aria-label*="dates"]'
    FILTER_GUESTS = 'button[aria-label*="guests"]'
    CARD = 'div[data-testid="card-container"]'  # updated selector
    RATING = '[aria-label$="rating"]'
    PRICE = 'span[data-testid="price"]'
    TITLE = 'div[role="heading"]'

    def wait_for_listings(self, timeout: int = 10000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        # ensure at least one card appears
        self.locator(self.CARD).first.wait_for(state="visible", timeout=timeout)

    def get_all_listings(self) -> List[Locator]:
        self.wait_for_listings()
        return self.locator(self.CARD).all()

    def get_first_listing(self) -> Locator:
        self.wait_for_listings()
        return self.locator(self.CARD).first

    def get_destination_filter_text(self) -> str:
        return self.get_text(self.FILTER_DEST)

    def get_dates_filter_text(self) -> str:
        return self.get_text(self.FILTER_DATES)

    def get_guests_filter_text(self) -> str:
        return self.get_text(self.FILTER_GUESTS)

    def get_rating(self, card: Locator) -> float:
        text = card.locator(self.RATING).inner_text().split()[0]
        return float(text)

    def get_price(self, card: Locator) -> float:
        text = card.locator(self.PRICE).inner_text().split()[0]
        return float(text)

    def get_title(self, card: Locator) -> str:
        return card.locator(self.TITLE).inner_text().strip()