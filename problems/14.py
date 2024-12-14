import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors

def get_collatz_chain_length(x: int, cached_collatz_chain_lengths: Dict[int, int]) -> List[int]:
    
    to_ret = 0
    target = x
    
    while target != 1:
        
        if target in cached_collatz_chain_lengths.keys():
            return to_ret + cached_collatz_chain_lengths[target]

        to_ret += 1
        if target / 2 == math.floor(target / 2):
            target = int(target / 2)
        else:
            target = 3 * target + 1
    to_ret += 1
    
    return to_ret

cached_collatz_chain_lengths: Dict[int, int] = {}
current_longest = (0,0)

for x in range(1, 1_000_000):

    len_collatz_chain = get_collatz_chain_length(x, cached_collatz_chain_lengths)
    
    if x not in cached_collatz_chain_lengths.keys():
        cached_collatz_chain_lengths[x] = len_collatz_chain
    
    if len_collatz_chain > current_longest[1]:
        current_longest = (x, len_collatz_chain)

    print(x, len_collatz_chain)


print(current_longest)