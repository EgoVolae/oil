import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

from utils.misc_number_theory import get_all_factors, get_prime_decomposition
from utils.misc_utils import timer


@timer
def __main__():

    results = []
    max_cycle_length = {0: 0}

    for divisor in range(2, 1000):

        divisions: Dict[int, Tuple] = {}  # Tuples of (divisor, dividend) that we've encountered
        division_index = 1

        leading_zeroes_in_result = math.ceil(math.log10(divisor)) - 1
        dividend = 10 ** (leading_zeroes_in_result + 1)
        decimal_rep = [0] * leading_zeroes_in_result

        division = (divisor, dividend)

        while division not in divisions.values():
            
            # Perform the division
            remainder = dividend % divisor
            quotient = int((dividend - remainder) / divisor)
            
            # Add what we've seen to lists
            decimal_rep.append(quotient)
            divisions[division_index] = division
            division_index += 1

            if remainder == 0:
                decimal_rep.append(-1)
                break

            # Calculate new dividend and divison we're performing
            more_zeroes = math.ceil(math.log10(divisor / remainder)) - 1
            decimal_rep.extend([0] * more_zeroes)

            dividend = remainder * (10 ** (more_zeroes + 1))
            division = (divisor, dividend)

        if decimal_rep[-1] != -1:
            current_division_index = division_index
            repeated_division_index = [k for k, v in divisions.items() if v == division][0]
            cycle_length = current_division_index - repeated_division_index
            
            results.append([divisor, cycle_length, decimal_rep])

            if cycle_length > list(max_cycle_length.values())[0]:
                max_cycle_length = {divisor: cycle_length}
        
    print(tabulate(results, headers=["Divisor", "Cycle", "Decimal Representation"], tablefmt="grid"))
    
    max_cycle_length_cycle = list(max_cycle_length.values())[0]
    max_cycle_length_divisor = list(max_cycle_length.keys())[0]

    print(f"Max cycle length = {max_cycle_length_cycle}, when divisor = {max_cycle_length_divisor}")
__main__()



# Do we need to perform long division here? Divide 7 into 10, take the remainder, etc.?