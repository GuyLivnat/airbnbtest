from typing import Tuple
from playwright.sync_api import Locator
from pages.search_results_page import SearchResultsPage


def find_cheapest_listing(results: SearchResultsPage) -> Tuple[Locator, int, str, str]:

    listings = results.get_all_listings()
    cheapest = min(listings, key=lambda c: results.get_price(c))
    price = results.get_price(cheapest)
    title = results.get_title(cheapest)
    name = results.get_name(cheapest)
    return cheapest, price, title, name


def find_highest_rated_listing(results: SearchResultsPage) -> Tuple[Locator, float, str, str]:

    listings = results.get_all_listings()
    best = max(listings, key=lambda c: results.get_rating(c))
    rating = results.get_rating(best)
    title = results.get_title(best)
    name = results.get_name(best)
    return best, rating, title, name
