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

    for x in range(1, 1000):
        
        situations = []  # Tuples of dividend, divisor that we've encountered

        log_10 = math.log10(x)
        higher_power_of_ten = 10 ** math.ceil(log_10)

        r = higher_power_of_ten % x
        q = int((higher_power_of_ten - r) / x)
        
        print(x,q,r)
        

__main__()



# Do we need to perform long division here? Divide 7 into 10, take the remainder, etc.?