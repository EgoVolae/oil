import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors

triangle_str = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

rows = [group.split(" ") for group in triangle_str.split("\n")[1:-1]]

# We can go from row_i[j] to row_{i+1}[j] or row_{i+1}[j+1]
# We can represent the first move with a 0 and the second move with a 1
# The paths are just going to be binary strings of length (num rows - 1)

def generate_binary_strings(x: int):
    if x == 1:
        return ["1","0"]
    return ["1" + x for x in generate_binary_strings(x - 1)] + ["0" + x for x in generate_binary_strings(x - 1)]

paths = generate_binary_strings(len(rows) - 1)

maximum_so_far = 0
for path in paths:
    path_total = 75
    current_pos = 0
    for i in range(1, len(rows)):
        row = rows[i]
        step = int(path[i-1])
        current_pos += step
        value = int(row[current_pos])
        path_total += value
    
    maximum_so_far = max(maximum_so_far, path_total)

print(maximum_so_far)


