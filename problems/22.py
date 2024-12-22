import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

project_root_dir = Path(__file__).parent.parent
print(project_root_dir)
with open(project_root_dir / "data_items/22_names.txt") as f:
    lines = f.readlines()

names = sorted(lines[0].split(","))

total = 0

for i, name in enumerate(names):
    score_temp = 0
    for char in name:
        if char not in scores.keys():
            continue
        score_temp += int(scores[char])

    name_score = (i + 1) * score_temp

    total += name_score

print(total)
