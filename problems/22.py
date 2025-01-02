import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors
import utils.misc_utils as mu

project_root_dir = Path(__file__).parent.parent

with open(project_root_dir / "data_items/22_names.txt") as f:
    lines = f.readlines()

names = sorted(lines[0].split(","))

total = 0

for i, name in enumerate(names):
    score_temp = 0
    for char in name:
        if char not in mu.LETTER_SCORES.keys():
            continue
        score_temp += int(mu.LETTER_SCORES[char])

    name_score = (i + 1) * score_temp

    total += name_score

print(total)
