from datetime import date, timedelta
from typing import Tuple

from playwright.sync_api import Locator

from pages.search_results_page import SearchResultsPage


def get_nearest_weekend() -> Tuple[date, date]:
    # Calculate nearest Thursday and Saturday
    today = date.today()
    thursday_offset = (3 - today.weekday() + 7) % 7 or 7
    saturday_offset = (5 - today.weekday() + 7) % 7 or 7
    thursday = (today + timedelta(days=thursday_offset))
    saturday = (today + timedelta(days=saturday_offset))

    return thursday, saturday

def get_cheapest_entry(data: dict[str, list]) -> dict[str, any]:
    prices = data["price"]
    cheapest = prices.index(min(prices))

    return {
        "title":  data["title"][cheapest],
        "name":   data["name"][cheapest],
        "price":  data["price"][cheapest],
        "rating": data["rating"][cheapest],
        "link":   data["link"][cheapest]
    }


def get_highest_rated_entry(data: dict[str, list]) -> dict[str, any]:
    ratings = data["rating"]
    highest_rated = ratings.index(max(ratings))

    return {
        "title":  data["title"][highest_rated],
        "name":   data["name"][highest_rated],
        "price":  data["price"][highest_rated],
        "rating": data["rating"][highest_rated],
        "link": data["link"][highest_rated]
    }


def collect_all_listings_data(results: SearchResultsPage) -> dict[str, list]:
    data: dict[str, list] = {"title": [], "name": [], "price": [], "rating": [], "link": []}
    # Ensure first page is loaded
    results.wait_for_listings()
    next_page = True
    while next_page:
        listings = results.get_all_listings()
        for card in listings:
            data["title"].append(results.get_title(card))
            data["name"].append(results.get_name(card))
            data["price"].append(results.get_price(card))
            data["rating"].append(results.get_rating(card))
            data["link"].append(results.get_href(card))

        next_page = results.click_next_page()
    return data


def print_listing(listing: dict):
    print(f"Title: {listing["title"]}.\n"
          f"Name: {listing["name"]}.\n"
          f"Price: {listing["price"]} NIS\n"
          f"Rating: {listing["rating"]}\n")


def get_child_text(parent: Locator) -> str:
    children = parent.locator("*").all()
    for child in children:
        text = child.inner_text().strip()
        if text:
            return text
    return ""
