import time
from typing import List, Tuple
from playwright.sync_api import Locator

from utils.helpers import get_child_text
from .base_page import BasePage


class RoomPage(BasePage):
    FULL_SIDEBAR = 'div[data-plugin-in-point-id="BOOK_IT_SIDEBAR"]'
    BOOK_SIDEBAR = 'div[data-section-id="BOOK_IT_SIDEBAR"]'
    BOOK_INFO = 'div[data-testid="book-it-default"]'
    CHECKIN = 'div[data-testid="change-dates-checkIn"]'
    CHECKOUT = 'div[data-testid="change-dates-checkOut"]'
    COUNT = 'div[id="GuestPicker-book_it-trigger"]'

    def get_info(self) -> dict:
        ppn = (self.locator(self.BOOK_INFO).locator("xpath=.//span[contains(text(), 'per night')]").first.inner_text())
        checkin = self.locator(self.CHECKIN).inner_text()
        checkout = self.locator(self.CHECKOUT).inner_text()
        g_count = self.locator(f"{self.COUNT} div span").inner_text().replace('\u00A0', ' ')
        sidebar = self.locator(self.FULL_SIDEBAR)
        fee_section = sidebar.locator("section").last
        sum_rows = fee_section.locator("div")
        nightly_sum = sum_rows.nth(0).locator("span").nth(3).inner_text()
        cleaning_fee = sum_rows.nth(0).locator("span").last.inner_text()
        spans = fee_section.locator("span")
        n = spans.count()
        total_fee = spans.nth(n-2).inner_text()

        return ({
            "price_per_night": ppn,
            "checkin": checkin,
            "checkout": checkout,
            "guest_count": g_count,
            "sum_nightly_fee": nightly_sum,
            "cleaning_fee": cleaning_fee,
            "total_fee": total_fee,
        })
