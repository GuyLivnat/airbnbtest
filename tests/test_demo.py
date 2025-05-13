import pytest
from datetime import date, timedelta
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.helpers import find_cheapest_listing, find_highest_rated_listing


def test_search_nearest_weekend(page):
    search_address = "Tel Aviv"
    home = HomePage(page)

    # Calculate nearest Friday and Saturday
    today = date.today()
    thursday_offset = (3 - today.weekday() + 7) % 7 or 7
    saturday_offset = (5 - today.weekday() + 7) % 7 or 7
    checkin_date = (today + timedelta(days=thursday_offset)).isoformat()
    checkout_date = (today + timedelta(days=saturday_offset)).isoformat()

    # Perform search flow
    home.search(search_address)
    home.select_date(checkin_date)
    home.select_date(checkout_date)
    home.select_guests(adults=2)
    home.submit_search()

    results = SearchResultsPage(page)
    cards = results.get_all_listings()
    assert cards is not None, "Expected at least one listing card"

    title = results.get_title(cards[0])

    _, price, title, name = find_cheapest_listing(results)
    print(f"The cheapest airbnb found for {search_address} is:\n"
          f"Title: {title}.\n"
          f"Name: {name}.\n"
          f"Price: {price}\n")

    _, rating, title, name = find_highest_rated_listing(results)
    print(f"The highest rated airbnb found for {search_address} is:\n"
          f"Title: {title}.\n"
          f"Name: {name}.\n"
          f"Rating: {rating}\n")

    # assert rating >= 0, "Invalid rating"
    # assert price >= 0, "Invalid price"
