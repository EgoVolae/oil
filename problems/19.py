import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors


WEEKDAYS = [0,1,2,3,4,5,6]
MONTHS_TO_DEFAULT_DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
YEARS = [year for year in range(1900, 2001)]

count = 0
weekday = 0
for year in YEARS:

    day_of_year = 0
    for month, num_days_in_month in MONTHS_TO_DEFAULT_DAYS.items():

        if month == 2 and year % 4 == 0:
            if year != 1900:
                num_days_in_month = 29

        for day_of_month in range(1, num_days_in_month + 1):
            print(weekday, month, day_of_month, year)
            if weekday == 6 and day_of_month == 1:
                if year != 1900:

                    count += 1

            day_of_year += 1
            weekday = (weekday + 1) % 7
    
print(count)