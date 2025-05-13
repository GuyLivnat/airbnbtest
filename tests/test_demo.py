import pytest
from datetime import date, timedelta
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_search_nearest_weekend(page):
    home = HomePage(page)

    # Calculate nearest Friday and Saturday
    today = date.today()
    friday_offset = (4 - today.weekday() + 7) % 7 or 7
    saturday_offset = (5 - today.weekday() + 7) % 7 or 7
    checkin_date = (today + timedelta(days=friday_offset)).isoformat()
    checkout_date = (today + timedelta(days=saturday_offset)).isoformat()

    # Perform search flow
    home.search("Tel Aviv")
    home.select_date(checkin_date)
    home.select_date(checkout_date)
    home.select_guests(adults=2)
    home.submit_search()

    # Initialize results and grab first listing (waits internally)
    results = SearchResultsPage(page)
    first_card = results.get_first_listing()
    assert first_card is not None, "Expected at least one listing card"

    # Log and assert basic details
    title = results.get_title(first_card)
    rating = results.get_rating(first_card)
    price = results.get_price(first_card)
    print(f"First listing: {title} — Rating: {rating}, Price: ${price}")
    assert rating >= 0, "Invalid rating"
    assert price >= 0, "Invalid price"
