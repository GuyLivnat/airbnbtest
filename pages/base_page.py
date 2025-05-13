from playwright.sync_api import Page, Locator


class BasePage:
    TIMEOUT = 10000

    def __init__(self, page: Page):
        self.page = page

    def goto(self, path: str = "/"):
        self.page.goto(path)

    def click(self, selector: str, timeout: int = TIMEOUT):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
        self.page.click(selector)

    def fill(self, selector: str, text: str, timeout: int = TIMEOUT):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.page.wait_for_selector(selector, state="visible")
        return self.page.inner_text(selector)

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)
