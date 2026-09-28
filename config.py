"""
System Configuration Constants
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR, "data", "trains.json")

# Initial counter seed for 10-digit unique PNR generation
INITIAL_PNR_COUNTER = 2004530060

# Booking status definitions
STATUS_CONFIRMED = "CONFIRMED"
STATUS_CANCELLED = "CANCELLED"