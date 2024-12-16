import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors

NUMBERS_TO_WORDS_MAP = {
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
    10: "TEN",
    11: "ELEVEN",
    12: "TWELVE",
    13: "THIRTEEN",
    14: "FOURTEEN",
    15: "FIFTEEN",
    16: "SIXTEEN",
    17: "SEVENTEEN",
    18: "EIGHTEEN",
    19: "NINETEEN",
    20: "TWENTY",
    30: "THIRTY",
    40: "FORTY",
    50: "FIFTY",
    60: "SIXTY",
    70: "SEVENTY",
    80: "EIGHTY",
    90: "NINETY",
    100: "HUNDRED",
    1000: "ONE THOUSAND"
}

def num_to_english_str(x: int) -> str:

    if x > 1000:
        raise Exception("Too big for this implementation!")
    
    if x == 1000:
        return NUMBERS_TO_WORDS_MAP[x]

    hundreds = x - x % 100
    tens = x - hundreds - x % 10 
    ones = x - hundreds - tens

    hundreds_str = ""
    hundreds_num = 0
    if hundreds != 0:
        hundreds_num = int(hundreds / 100)
        hundreds_str = f"{NUMBERS_TO_WORDS_MAP[hundreds_num]} HUNDRED"

    and_str = ""
    if hundreds != 0 and (tens != 0 or ones != 0):
        and_str = "AND"

    tens_str = ""
    tens_num = 0
    if tens != 0:
        tens_num = int(tens / 10)
        if tens_num == 1:
            tens_str = f"{NUMBERS_TO_WORDS_MAP[tens + ones]}"
        else:
            tens_str = f"{NUMBERS_TO_WORDS_MAP[tens]}"

    ones_str = ""
    if ones != 0 and tens_num != 1:
        ones_str = f"{NUMBERS_TO_WORDS_MAP[ones]}"
    
    return hundreds_str + " " + and_str + " " + tens_str + " " + ones_str

to_ret = 0
for i in range(1,1001):
    
    english_str = num_to_english_str(i)
    num_chars = len(english_str.replace(" ",""))
    print(english_str, num_chars)
    to_ret += num_chars

print(to_ret)
