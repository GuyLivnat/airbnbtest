# from datetime import date, timedelta
# from pages.home_page import HomePage
# from pages.search_results_page import SearchResultsPage
# from utils.helpers import collect_all_listings_data, get_cheapest_entry, get_highest_rated_entry, print_listing, \
#     get_nearest_weekend
#
#
# def test_case_2(page):
#     # Init
#     search_address = "Tel Aviv"
#     home = HomePage(page)
#     checkin_date, checkout_date = get_nearest_weekend()
#
#     # Perform search flow
#     home.search(search_address)
#     home.select_date(checkin_date)
#     home.select_date(checkout_date)
#     home.select_guests(adults=2)
#     home.submit_search()
#
#     # Validate output
#     results = SearchResultsPage(page)
#     cards = results.get_all_listings()
#     assert cards is not None, "Expected at least one listing card"
#
#     # Parse data into a dict for local use
#     data = collect_all_listings_data(results)
#
#     # Print output
#     print(f"Test Case 1:\n"
#           f"Below results are from the date {checkin_date} until {checkout_date}\n")
#
#     cheapest = get_cheapest_entry(data)
#     print(f"The cheapest airbnb found for '{search_address}' is:\n")
#     print_listing(cheapest)
#
#     highest_rated = get_highest_rated_entry(data)
#     print(f"The highest rated airbnb found for '{search_address}' is:\n")
#     print_listing(highest_rated)
