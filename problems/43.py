import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
import itertools
from tabulate import tabulate

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0

    first_7_primes = mnt.get_list_of_primes(7)

    digits_0_to_9 = [str(x) for x in range(10)]

    for perm in itertools.permutations(digits_0_to_9):
        
        success = True

        if perm[0] == "0":
            continue
            
        for start_idx in range(1, 8):

            number = int("".join(perm[start_idx: start_idx + 3]))
            prime_to_test = first_7_primes[start_idx - 1]

            if number % prime_to_test != 0:
                success = False
                break
                        
        if success:
            full_number = int("".join(perm))
            answer += full_number
            print(full_number)

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")