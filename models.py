"""
Data Storage & Models Manager
Handles in-memory data structures and data file loading.
"""

import json
import os
from config import DATA_FILE_PATH, INITIAL_PNR_COUNTER


class RailwayDatabase:
    """Manages system state for trains, active bookings, and PNR counters."""

    def __init__(self):
        self.trains = self._load_trains()
        self.bookings = []
        self.pnr_counter = INITIAL_PNR_COUNTER

    def _load_trains(self):
        """Load initial train details from JSON file or fallback defaults."""
        if os.path.exists(DATA_FILE_PATH):
            try:
                with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                pass

        # Default fallback dataset
        return [
            {
                "number": "12301",
                "name": "Howrah Rajdhani",
                "source": "Delhi",
                "destination": "Kolkata",
                "departure": "16:55",
                "total_seats": 10,
                "fare": 1850,
            },
            {
                "number": "12951",
                "name": "Pushpak Express",
                "source": "Lucknow",
                "destination": "Mumbai",
                "departure": "21:25",
                "total_seats": 16,
                "fare": 2100,
            },
            {
                "number": "12009",
                "name": "Shatabdi Express",
                "source": "Delhi",
                "destination": "Bhopal",
                "departure": "06:15",
                "total_seats": 10,
                "fare": 950,
            },
            {
                "number": "12358",
                "name": "Durgiana Express",
                "source": "Lucknow",
                "destination": "Kolkata",
                "departure": "20:15",
                "total_seats": 20,
                "fare": 1950,
            },
        ]

    def get_next_pnr(self):
        """Generate and increment unique PNR number."""
        current = self.pnr_counter
        self.pnr_counter += 1
        return current


# Global database instance initialized on module import
db = RailwayDatabase()