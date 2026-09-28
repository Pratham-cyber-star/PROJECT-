"""
CLI User Interface & Menu Controllers
Handles passenger interactions, menu navigation, and input sanitization.
"""

from booking_service import (
    book_ticket,
    cancel_ticket,
    get_bookings_by_name,
    get_occupancy_data,
    get_revenue_data,
    get_seats_left,
    search_trains,
    show_all_trains,
)


def get_valid_int(prompt_text):
    """Prompt user repeatedly until a valid integer is entered."""
    while True:
        user_input = input(prompt_text).strip()
        if user_input.isdigit():
            return int(user_input)
        print("Please enter a valid number.")


def booking_menu():
    """Interactive workflow for searching and booking train tickets."""
    print("\n----- Book a Ticket -----")
    source = input("From: ").strip()
    destination = input("To: ").strip()

    matching_trains = search_trains(source, destination)
    if not matching_trains:
        print("No trains found on this route.")
        return

    print(f"\n{'#':<4}{'Number':<10}{'Name':<20}{'Fare':<8}{'Seats Left'}")
    for idx, train in enumerate(matching_trains, start=1):
        seats_left = get_seats_left(train["number"])
        print(
            f"{idx:<4}{train['number']:<10}{train['name']:<20}{train['fare']:<8}{seats_left}"
        )

    choice = get_valid_int("\nSelect option number from list (0 to cancel): ")
    if choice == 0 or choice > len(matching_trains):
        return

    selected_train = matching_trains[choice - 1]

    name = input("Passenger name: ").strip()
    age = get_valid_int("Age: ")
    gender = input("Gender (M/F/O): ").strip().upper()

    pnr = book_ticket(selected_train["number"], name, age, gender)
    if pnr is not None:
        print(f"\nBooking confirmed! Your PNR is {pnr}. Keep this safe.")


def cancel_menu():
    """Interactive workflow for ticket cancellation."""
    print("\n----- Cancel a Ticket -----")
    pnr = get_valid_int("Enter your PNR number: ")
    if cancel_ticket(pnr):
        print("Your ticket has been cancelled successfully.")


def view_menu():
    """Interactive lookup of bookings by passenger name."""
    print("\n----- View My Bookings -----")
    name = input("Enter your name: ").strip()
    results = get_bookings_by_name(name)

    print(f"\n----- Bookings for {name} -----")
    if not results:
        print("No bookings found under this name.")
        return

    for booking, train in results:
        train_name = train["name"] if train else "Unknown Train"
        print(
            f"PNR: {booking['pnr']} | {train_name:<18} | Seat {booking['seat_number']} "
            f"| Status: {booking['status']}"
        )


def show_occupancy_report():
    """Render occupancy report."""
    print("\n----- Occupancy Report -----")
    data = get_occupancy_data()
    for name, booked, total in data:
        print(f"{name:<20} {booked}/{total} seats booked")


def show_revenue_report():
    """Render financial revenue report."""
    print("\n----- Revenue Report -----")
    data, total_revenue = get_revenue_data()
    for name, tickets_sold, revenue in data:
        print(f"{name:<20} {tickets_sold} tickets   Rs.{revenue}")
    print(f"\nTotal revenue: Rs.{total_revenue}")


def admin_menu():
    """Administrative submenu loop."""
    while True:
        print("\n===== Admin Menu =====")
        print("1. Show All Trains")
        print("2. Occupancy Report")
        print("3. Revenue Report")
        print("4. Back to Main Menu")
        choice = get_valid_int("Choose an option: ")

        if choice == 1:
            show_all_trains()
        elif choice == 2:
            show_occupancy_report()
        elif choice == 3:
            show_revenue_report()
        elif choice == 4:
            break
        else:
            print("Invalid choice, try again.")


def main_menu():
    """Root main loop of the application CLI."""
    while True:
        print("\n===== RAILWAY RESERVATION SYSTEM =====")
        print("1. Show All Trains")
        print("2. Book a Ticket")
        print("3. Cancel a Ticket")
        print("4. View My Bookings")
        print("5. Admin Menu")
        print("6. Exit")
        choice = get_valid_int("Choose an option: ")

        if choice == 1:
            show_all_trains()
        elif choice == 2:
            booking_menu()
        elif choice == 3:
            cancel_menu()
        elif choice == 4:
            view_menu()
        elif choice == 5:
            admin_menu()
        elif choice == 6:
            print("Thank you for using the Railway Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")