from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage
from pages.room_page import RoomPage
from pages.search_results_page import SearchResultsPage
from utils.helpers import collect_all_listings_data, get_cheapest_entry, get_highest_rated_entry, print_listing, \
    get_nearest_weekend


def test_case_2(page):
    # Init
    search_address = "Tel Aviv"
    home = HomePage(page)
    checkin_date, checkout_date = get_nearest_weekend()
    adult_count = 2
    child_count = 1
    guest_count = adult_count + child_count

    # Perform search flow
    home.search(search_address)
    home.select_date(checkin_date.isoformat())
    home.select_date(checkout_date.isoformat())
    home.select_guests(adults=adult_count, children=child_count)
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

    # Continue flow
    highest_rated = get_highest_rated_entry(data)
    results.goto(highest_rated["link"])

    room = RoomPage(page)

    # Reservation details
    info = room.get_info()
    print(f"Here are the details for the top rated airbnb in '{search_address}':\n"
          f"The cost is {info["price_per_night"]}\n"
          f"Check in is on {info["checkin"]}\n"
          f"Check out is on {info["checkout"]}\n"
          f"A total of {info["guest_count"]} will be attending\n"
          f"The sum of the nightly costs is {info["sum_nightly_fee"]}\n"
          f"There is an additional fee of {info["cleaning_fee"]}\n"
          f"The sum total cost is {info["total_fee"]}\n")

    # Attempt reservation
    room.confirm()

    conf = ConfirmationPage(page)
    f_count = conf.get_guest_count()
    f_date = conf.get_dates()
    f_date = f_date.split()

    #
    assert str(guest_count) in f_count
    assert f_date[1] == checkin_date.strftime("%b")
    assert f_date[2] == checkin_date.strftime("%d")
    assert f_date[4] == checkout_date.strftime("%d")
    conf.choose_country("972IL")
    conf.input_phone_number(80815808)
    page.pause()

