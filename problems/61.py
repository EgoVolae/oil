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

    P_3s = {str(y) for y in [int((x * (x + 1 )) / 2) for x in range(1000)] if 1000 <= y <= 9999}
    P_4s = {str(y) for y in [int(x ** 2) for x in range(1000)] if 1000 <= y <= 9999}
    P_5s = {str(y) for y in [int((x * (3 * x - 1 )) / 2) for x in range(1000)] if 1000 <= y <= 9999}
    P_6s = {str(y) for y in [int(x * (2 * x - 1 )) for x in range(1000)] if 1000 <= y <= 9999}
    P_7s = {str(y) for y in [int((x * (5 * x - 3 )) / 2) for x in range(1000)] if 1000 <= y <= 9999}
    P_8s = {str(y) for y in [int(x * (3 * x - 2 )) for x in range(1000)] if 1000 <= y <= 9999}

    everything = P_3s.union(P_4s, P_5s, P_6s, P_7s, P_8s)
    
    chains = []
    for connection in range(10, 100):
        
        conn = str(connection)

        l_1_candidates = {i for i in everything if i[:2] == conn}
        
        for l_1 in l_1_candidates:

            conn_1_2 = l_1[2:]
            l_2_candidates = {i for i in everything if i[:2] == conn_1_2}

            for l_2 in l_2_candidates:

                conn_2_3 = l_2[2:]
                l_3_candidates = {i for i in everything if i[:2] == conn_2_3}

                for l_3 in l_3_candidates:

                    conn_3_4 = l_3[2:]
                    l_4_candidates = {i for i in everything if i[:2] == conn_3_4}

                    for l_4 in l_4_candidates:

                        conn_4_5 = l_4[2:]
                        l_5_candidates = {i for i in everything if i[:2] == conn_4_5}

                        for l_5 in l_5_candidates:

                            conn_5_6 = l_5[2:]
                            l_6_candidates = {i for i in everything if i[:2] == conn_5_6}

                            for l_6 in l_6_candidates:

                                if l_6[2:] == l_1[:2]:
                                    chains.append([l_1, l_2, l_3, l_4, l_5, l_6])
    
    print(f"Chains before removing doubles: {len(chains)}")
    chains = [c for c in chains if len(set(c)) == len(c)]
    print(f"Chains after removing doubles: {len(chains)}")

    for chain in chains:

        venns = [frozenset(family.intersection(set(chain))) for family in [P_3s, P_4s, P_5s, P_6s, P_7s, P_8s]]
        
        if frozenset() in venns:
            continue
        
        if len(set(venns)) != len(venns):
            continue
        
        print(chain)
        answer = sum([int(elem) for elem in chain])
        return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")