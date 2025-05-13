from playwright.sync_api import Page, Locator


class BasePage:

    def __init__(self, page: Page, base_url: str = "https://www.airbnb.com"):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = "/"):
        url = path if path.startswith("http") else f"{self.base_url}{path}"
        self.page.goto(url)

    def click(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
        self.page.click(selector)

    def fill(self, selector: str, text: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.page.wait_for_selector(selector, state="visible")
        return self.page.inner_text(selector)

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)
