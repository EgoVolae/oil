import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():
    
    triangle_numbers = [0.5 * n * (n + 1) for n in range(1, 50)]

    project_root_dir = Path(__file__).parent.parent
    
    with open(project_root_dir / "data_items/42_words.txt") as f:
        lines = f.readlines()

    words = sorted(lines[0].split(","))

    count = 0

    for word in words:

        score = sum([mu.LETTER_SCORES[char] for char in word if char != '"'])
        
        if score in triangle_numbers:
            print(word, score)

            count += 1

    return count

answer = __main__()

print(f"{answer=}")

question_num = __file__.split("\\")[-1].split(".")[0]
print(question_num)
