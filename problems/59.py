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

    project_root_dir = Path(__file__).parent.parent
    
    with open(project_root_dir / "data_items/59_cipher.txt") as f:
        lines = f.readlines()

    encrypted_chars = bytes([int(x) for x in lines[0].split(",")])

    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):

                key = bytes([i, j, k])

                decryption_bytes = key * math.ceil(len(encrypted_chars) / 3)

                plaintext = bytes(a ^ b for a, b in zip(decryption_bytes, encrypted_chars))

                if bytes("the", "ascii") in plaintext:
                    if bytes("and", "ascii") in plaintext:
                        if bytes("this", "ascii") in plaintext:
                            print(key)

                            print(sum(key))

                            print(plaintext)

    return

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")