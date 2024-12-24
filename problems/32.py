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
    
    DIGITS = {str(x) for x in range(1, 10)}

    MIN_PRODUCT = 1001
    MAX_PRODUCT = 9999

    results = []

    for x in range(MIN_PRODUCT, MAX_PRODUCT + 1):
    # for x in range(7253,7255):

        x_digits = list(str(x))
        unique_x_digits = set(x_digits)

        if len(unique_x_digits) != len(x_digits):
            continue

        factors = get_all_factors(x)

        for m in factors:
            n = int (x / m)

            m_digits = list(str(m))
            n_digits = list(str(n))

            unique_m_digits = set(m_digits)
            unique_n_digits = set(n_digits)

            if (len(unique_m_digits) != len(m_digits)) or (len(unique_n_digits) != len(n_digits)):
                continue

            if len(unique_m_digits) + len(unique_n_digits) + len(unique_x_digits) == len(DIGITS):

                if unique_x_digits.union(unique_m_digits).union(unique_n_digits) == DIGITS:
                    print(f"Found triple: {x, m, n}")
                    
                    current_xs = [triple[0] for triple in results]
                    if x not in current_xs:
                        results.append([x, m, n])
        
    print(results)
    answer = sum([triple[0] for triple in results])
    print(f"answer={answer}")


__main__()
