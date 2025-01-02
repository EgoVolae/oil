import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
import itertools
import numpy as np
from collections import defaultdict

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    prime_strings = [str(x) for x in range(1_000_000) if mnt.lazy_is_prime(x)]
    print(f"Found {len(prime_strings)} primes")

    for number_length in [5,6]:
        print(f"Trying number length: {number_length}")
        
        for combo_length in range(1, number_length):
            print(f"Trying combo length: {combo_length}")
        
            for combo in itertools.combinations(range(number_length - 1), r=combo_length):
                
                families_for_combo: Dict[str, int] = defaultdict(lambda: 0)

                for p_str in prime_strings:

                    if len(p_str) != number_length:
                        continue

                    if not len(set([p_str[k] for k in range(len(p_str)) if k in combo])) == 1:
                        continue

                    remaining_num = "".join([p_str[k] for k in range(len(p_str)) if k not in combo])
                    
                    families_for_combo[remaining_num] += 1
                    
                if max(families_for_combo.values()) == 8:
                    
                    remaining_num = [k for k, v in families_for_combo.items() if v == 8][0]
                    family_members = [p_str for p_str in prime_strings if "".join([p_str[k] for k in range(len(p_str)) if k not in combo]) == remaining_num and len(set([p_str[k] for k in range(len(p_str)) if k in combo])) == 1]
                    
                    print(f"Family of size 8: {family_members} when {number_length=} and {combo=}!")
                    
                    return min(family_members)
        
answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")