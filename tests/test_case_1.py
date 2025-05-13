from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.helpers import collect_all_listings_data, get_cheapest_entry, get_highest_rated_entry, print_listing, \
    get_nearest_weekend


def test_case_1(page):
    # Init
    search_address = "Tel Aviv"
    home = HomePage(page)
    checkin_date, checkout_date = get_nearest_weekend()
    guest_count = 2

    # Perform search flow
    home.search(search_address)
    home.select_date(checkin_date.isoformat())
    home.select_date(checkout_date.isoformat())
    home.select_guests(adults=guest_count)
    home.submit_search()

    # Validate output
    results = SearchResultsPage(page)
    f_location, f_date, f_count = results.get_current_search_settings()
    f_date = f_date.split()
    assert search_address in f_location
    assert str(guest_count) in f_count
    assert f_date[0] == checkin_date.strftime("%b")
    assert f_date[1] == checkin_date.strftime("%d")
    assert f_date[3] == checkout_date.strftime("%d")

    cards = results.get_all_listings()
    assert cards is not None, "Expected at least one listing card"

    # Parse data into a dict for local use
    data = collect_all_listings_data(results)

    # Print output
    print(f"Test Case 1:\n"
          f"Below results are for the dates {checkin_date} though {checkout_date}\n")

    cheapest = get_cheapest_entry(data)
    print(f"The cheapest airbnb found for '{search_address}' is:\n")
    print_listing(cheapest)

    highest_rated = get_highest_rated_entry(data)
    print(f"The highest rated airbnb found for '{search_address}' is:\n")
    print_listing(highest_rated)
