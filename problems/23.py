import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors, get_prime_decomposition
from utils.misc_utils import timer

@timer
def __main__():


    unsummable = []
    abundant_numbers = []
    odd_abundant_numbers = []
    even_abundant_numbers = []

    # for x in range(1, 28123):

    #     factor_sum = sum(get_all_factors(x, proper=True))
    #     if factor_sum > x:
    #         abundant_numbers.append(x)

    # odd_abundant_numbers = [x for x in abundant_numbers if x % 2 != 0]
    # for x in odd_abundant_numbers:
    #     print(f"{x}: {get_prime_decomposition(x)}")


    for x in range(1, 28123):

        is_even = x % 2 == 0
        # Populating abundant number running list

        factor_sum = sum(get_all_factors(x, proper=True))
        if factor_sum > x:
            abundant_numbers.append(x)
            if is_even:
                even_abundant_numbers.append(x)
            else:
                odd_abundant_numbers.append(x)

        summable = False
        abundant_numbers_less_than_half_x = [y for y in abundant_numbers if y <= x / 2]

        if is_even:

            for m in abundant_numbers_less_than_half_x:
                if m % 2 == 0:
                    if (x - m) in even_abundant_numbers:
                        summable = True
                        break            
                if m % 2 == 1:
                    if (x - m) in odd_abundant_numbers:
                        summable = True
                        break
        
        if not is_even:

            for m in odd_abundant_numbers:
                if (x - m) in even_abundant_numbers:
                    summable = True
                    break

        if not summable:
            print(f"{x} is not summable")
            unsummable.append(x)
            

    print(len(unsummable))
    print(sum(unsummable))

    ### Is every abundant number even? Not true

__main__()
