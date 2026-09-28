"""
Business Logic & Service Layer
Handles train queries, seat availability, ticket bookings, cancellations, and reports.
"""

from config import STATUS_CANCELLED, STATUS_CONFIRMED
from models import db


def find_train(train_number):
    """Find and return train dictionary by train number or None."""
    for train in db.trains:
        if train["number"] == train_number:
            return train
    return None


def get_seats_left(train_number):
    """Calculate total remaining seats for a given train."""
    train = find_train(train_number)
    if not train:
        return 0

    booked_count = sum(
        1
        for booking in db.bookings
        if booking["train_number"] == train_number
        and booking["status"] == STATUS_CONFIRMED
    )
    return train["total_seats"] - booked_count


def search_trains(source, destination):
    """Filter trains matching source and destination (case-insensitive)."""
    return [
        train
        for train in db.trains
        if train["source"].lower() == source.lower()
        and train["destination"].lower() == destination.lower()
    ]


def show_all_trains():
    """Display complete train schedule along with live seat availability."""
    print("\n-- All Trains --")
    print(
        f"{'No.':<8}{'Name':<20}{'From':<10}{'To':<10}{'Time':<8}{'Fare':<8}{'Seats Left'}"
    )
    for train in db.trains:
        seats_left = get_seats_left(train["number"])
        print(
            f"{train['number']:<8}{train['name']:<20}{train['source']:<10}"
            f"{train['destination']:<10}{train['departure']:<8}{train['fare']:<8}{seats_left}"
        )


def book_ticket(train_number, passenger_name, age, gender):
    """
    Reserve a seat on a train.
    Assigns the lowest unused sequential seat number.
    Returns PNR on success or None if train is fully booked.
    """
    seats_left = get_seats_left(train_number)
    if seats_left <= 0:
        print("Sorry, this train is fully booked.")
        return None

    taken_seats = [
        booking["seat_number"]
        for booking in db.bookings
        if booking["train_number"] == train_number
        and booking["status"] == STATUS_CONFIRMED
    ]

    seat_number = 1
    while seat_number in taken_seats:
        seat_number += 1

    pnr = db.get_next_pnr()
    new_booking = {
        "pnr": pnr,
        "train_number": train_number,
        "passenger_name": passenger_name,
        "age": age,
        "gender": gender,
        "seat_number": seat_number,
        "status": STATUS_CONFIRMED,
    }
    db.bookings.append(new_booking)
    return pnr


def cancel_ticket(pnr):
    """Cancel booking by PNR number. Returns True if cancelled, False otherwise."""
    for booking in db.bookings:
        if booking["pnr"] == pnr:
            if booking["status"] == STATUS_CANCELLED:
                print("This ticket is already cancelled.")
                return False
            booking["status"] = STATUS_CANCELLED
            return True

    print("No booking found with that PNR.")
    return False


def get_bookings_by_name(passenger_name):
    """Retrieve all bookings under a specific passenger name."""
    matching_bookings = []
    for booking in db.bookings:
        if booking["passenger_name"].lower() == passenger_name.lower():
            train = find_train(booking["train_number"])
            matching_bookings.append((booking, train))
    return matching_bookings


def get_occupancy_data():
    """Generate occupancy stats for administrative reports."""
    report = []
    for train in db.trains:
        seats_left = get_seats_left(train["number"])
        booked = train["total_seats"] - seats_left
        report.append((train["name"], booked, train["total_seats"]))
    return report


def get_revenue_data():
    """Calculate earnings per train route based on confirmed bookings."""
    report = []
    total_revenue = 0

    for train in db.trains:
        tickets_sold = sum(
            1
            for booking in db.bookings
            if booking["train_number"] == train["number"]
            and booking["status"] == STATUS_CONFIRMED
        )
        revenue = tickets_sold * train["fare"]
        total_revenue += revenue
        report.append((train["name"], tickets_sold, revenue))

    return report, total_revenue