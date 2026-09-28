# Railway Ticket Reservation System

An interactive, command-line interface (CLI) application built in Python that simulates a train ticketing and reservation system. The application handles real-time seat availability, ticket bookings with auto-generated PNR numbers, cancellations, passenger search, and administrative reports for train occupancy and revenue.

---

## Overview

The **Railway Ticket Reservation System** provides a simple workflow for passengers and railway administrators:

* **Passengers** can check available trains between cities, search routes, reserve seats, view active bookings, and cancel tickets.
* **Administrators** can view total system occupancy and track revenue generated per train route.

The program runs in a terminal loop and uses in-memory Python data structures (`lists` and `dictionaries`) to maintain real-time state during execution.

---

## Features

### 🚆 Passenger Management

* **View All Trains:** Lists all available trains, departure times, fares, and real-time remaining seat counts.
* **Search by Route:** Finds matching trains based on origin (source) and destination cities (case-insensitive).
* **Ticket Booking:**
* Auto-assigns the lowest available sequential seat number (1, 2, 3, ...).
* Generates a unique 10-digit PNR number.
* Prevents overbooking when a train reaches maximum capacity.


* **Ticket Cancellation:** Updates booking status to `CANCELLED` and immediately releases the seat back into the available pool.
* **Lookup Bookings:** Search and view all confirmed/cancelled tickets under a passenger's name.

### 📊 Admin Module

* **Occupancy Report:** Displays current seat utilization (`booked / total_seats`) for every train.
* **Revenue Report:** Calculates total financial earnings per train route based on confirmed bookings and fare prices.

### 🛡️ Reliability & Input Handling

* **Input Validation:** Prevents program crashes when numeric choices or age values are expected (`get_valid_int`).

---

## Technologies & Tools Used

| Tool / Tech | Details |
| --- | --- |
| **Language** | Python 3.x |
| **Libraries** | Python Standard Library (no external pip dependencies required) |
| **Data Structures** | In-memory `lists` and `dicts` |
| **Interface** | Terminal / Command-Line Interface (CLI) |

---

## Installation & Execution

### Prerequisites

* **Python 3.6+** installed on your system. Verify by running:
```bash
python --version
# or
python3 --version

```



### Steps to Run

1. **Clone or Download the Repository:**
```bash
git clone https://github.com/your-username/railway-reservation-system.git
cd railway-reservation-system

```


2. **Create the Script File:**
Save the Python code into a file named `railway_system.py`.
3. **Execute the Application:**
```bash
python railway_system.py

```



> **Note on Code Corrections:**
> If running the initial code snippet, ensure the following two function name calls are aligned:
> 1. In `get_seats_left()`, rename `find_train_by_number(...)` to `find_train(...)`.
> 2. In `admin_menu()` and `main_menu()`, rename `show_all_trains()` to `show__trains()`.
> 
> 

---

## Instructions for Testing

Follow these step-by-step test cases in the CLI menu to verify system functionality:

### Test Case 1: Search and Book a Ticket

1. Run the script and select option `2` (**Book a Ticket**).
2. Enter **Source:** `Delhi` and **Destination:** `Kolkata`.
3. Choose train option `1` (Howrah Rajdhani).
4. Enter passenger details (e.g., Name: `Alice`, Age: `28`, Gender: `F`).
5. **Expected Result:** Ticket is booked, PNR `2004530060` is displayed, and seat number `1` is assigned.

### Test Case 2: Verify Seat Count Reduction & Lookup

1. Select option `4` (**View My Bookings**) from the main menu and enter `Alice`.
* **Expected Result:** Shows active PNR, train name, seat number, and `CONFIRMED` status.


2. Select option `1` (**Show All Trains**).
* **Expected Result:** Seats left for Howrah Rajdhani should decrease from `10` to `9`.



### Test Case 3: Admin Reports

1. Select option `5` (**Admin Menu**).
2. Select `2` (**Occupancy Report**).
* **Expected Result:** Shows `1/10 seats booked` for Howrah Rajdhani.


3. Select `3` (**Revenue Report**).
* **Expected Result:** Displays revenue of `Rs. 1850` for Howrah Rajdhani and total revenue of `Rs. 1850`.



### Test Case 4: Cancel Ticket

1. Return to the main menu and select option `3` (**Cancel a Ticket**).
2. Enter PNR: `2004530060`.
* **Expected Result:** "Your ticket has been cancelled." message appears.


3. Re-check **Admin Occupancy Report** or **Show All Trains**.
* **Expected Result:** Available seats return to `10`, and revenue updates back to `0`.



---

## Screenshots & Sample CLI Output

### Main Menu

```text
===== RAILWAY RESERVATION SYSTEM =====
1. Show All Trains
2. Book a Ticket
3. Cancel a Ticket
4. View My Bookings
5. Admin Menu
6. Exit
Choose an option: 1

-- All Trains --
No.     Name                From      To        Time    Fare    Seats Left
12301   Howrah Rajdhani     Delhi     Kolkata   16:55   1850    10
12951   Pushpak Express     Lucknow   Mumbai    21:25   2100    16
12009   Shatabdi Express    Delhi     Bhopal    06:15   950     10
12358   Durgiana Express    Lucknow   Kolkata   20:15   1950    20

```

### Booking Flow

```text
----- Book a Ticket -----
From: Delhi
To: Kolkata

#   Number    Name                Fare    Seats Left
1   12301     Howrah Rajdhani     1850    10

Select train number from list (0 to cancel): 1
Passenger name: John Doe
Age: 30
Gender (M/F/O): M

Booking confirmed! Your PNR is 2004530060. Keep this safe.

```

### Admin Reports Output

```text
----- Occupancy Report -----
Howrah Rajdhani      1/10 seats booked
Pushpak Express      0/16 seats booked
Shatabdi Express     0/10 seats booked
Durgiana Express     0/20 seats booked

----- Revenue Report -----
Howrah Rajdhani      1 tickets   Rs.1850
Pushpak Express      0 tickets   Rs.0
Shatabdi Express     0 tickets   Rs.0
Durgiana Express     0 tickets   Rs.0

Total revenue: Rs.1850

```
