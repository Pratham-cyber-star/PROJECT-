# Statement of Work & Project Definition

## Problem Statement

Traditional manual train ticketing processes and unintegrated booking methods often lead to severe operational bottlenecks, including overbooking errors, lack of real-time seat visibility, and cumbersome financial reconciliation. Without an automated management framework, tracking seat availability, generating unique passenger identifiers (PNRs), and evaluating route profitability require manual oversight that is prone to human error.

The **Railway Ticket Reservation System** addresses this problem by providing a centralized, automated terminal-based solution. It streamlines train selection, automates sequential seat allocation, processes instant cancellations, and generates real-time occupancy and revenue reports.

---

## Scope of the Project

### In-Scope

* **Train Schedule Management:** Displaying predefined train routes, timings, fares, and total capacities.
* **Route Querying:** Case-insensitive search filtering for matching source and destination pairs.
* **Seat Allocation & Inventory Control:** Real-time availability calculations and automatic sequential seat assignment (e.g., Seat 1, Seat 2) per train.
* **Ticketing Lifecycle:** Ticket booking with unique 10-digit PNR generation, cancellation processing, and status toggling (`CONFIRMED` / `CANCELLED`).
* **Passenger Records:** Querying active and past bookings by passenger name.
* **Administrative Analytics:** Route-by-route seat occupancy metrics and cumulative revenue calculation.
* **Robust CLI Interface:** Terminal menu driven by sanitized input validation (`get_valid_int`) to prevent runtime exceptions.

### Out-of-Scope (Future Expansion)

* Persistent database storage (PostgreSQL/SQLite) or file persistence (JSON/CSV) across application restarts.
* Graphical User Interface (GUI) or Web-based frontend.
* Multi-user concurrent session management and role-based authentication logins.
* Payment gateway integration and dynamic pricing algorithms.
* Complex berth/seat selection preferences (e.g., Lower, Middle, Upper, Side-Lower).

---

## Target Users

| User Category | Description & Primary Actions |
| --- | --- |
| **Passengers / Travelers** | Primary consumers who query train schedules, search available routes, book seats, view active bookings, and cancel existing tickets. |
| **Railway Operations Administrators** | Internal staff who monitor operational metrics, track train occupancy percentages, and review route sales and financial summaries. |
| **Developers & Academic Evaluators** | Technical personnel assessing modular Python architecture, standard data structure implementations (`list` of `dict`), and algorithm efficiency. |

---

## High-Level Features

* **Route Search & Schedule Discovery:** Fast lookup mechanism filtering trains based on departure and destination inputs, returning live fare and remaining seat data.
* **Automated Seat Assignment:** Sequential seat allocation engine that identifies the lowest available seat number and blocks overbooking when capacity reaches zero.
* **PNR Management System:** Automated generation of 10-digit PNR tracking numbers linked to passenger demographics (Name, Age, Gender).
* **Instant Cancellation & Inventory Release:** Status-driven ticket cancellation system that immediately returns freed seats back to the public booking pool.
* **Passenger Search Lookup:** Retrieve all confirmed or cancelled tickets associated with a specific passenger name.
* **Occupancy & Financial Reporting:** Real-time administrative reporting engine displaying seat fill rates ($Booked / Total$) and gross revenue generated per route.
