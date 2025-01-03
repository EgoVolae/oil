import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
import itertools
import numpy as np

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():
    
    answer = 0
    n = 11
    for B in range(1, n+1):
        for r in range(n + 1):

            if B == 1:
                answer += 1
                continue

            c = math.comb(n, r)
            print(f"{r=}, {B=}, {c=}")

            ### S_B(x) is just going to be the product of all the primes up to and including B
            ### that appear in the decomposition
            prime_decomp = mnt.get_prime_decomposition(c)


            ### Decomposition looks like [2,2,2,3,3,5,7,13,23,37] for example. If this is the decomposition for x,
            ### S_B(x) = x when B >= 37. We can sum up across all B up to x fairly easily

            ### Decomposition is [q_1, q_2, q_3,...,q_k], where q_i is the power of p_i in the representation
            ### Let d_i = p_i - p_{i-1} (the distance between primes)
            ### We have sum S_B(x) B=1 -> B=n = 1 + [prod(q_1,...,q_i-1) * d_i for i = 1 to k ] + (x - p_k + 1) * x

            ### For x = 30 = [2,3,5] = [1,1,1] = 1 + [2 + 2*3 + 2*3] + 26*30

            print(f"{prime_decomp=}")
            S_B_c = math.prod([p for p in prime_decomp if p <= B])

            answer += S_B_c
            print(f"For decomposing {c}, we have that factor {S_B_c} is {B}-smooth")
            
    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")