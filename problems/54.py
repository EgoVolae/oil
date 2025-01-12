import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Set, Tuple
import math
from tabulate import tabulate
from dataclasses import dataclass
import itertools
import numpy as np
from enum import Enum

import utils.misc_number_theory as mnt
import utils.misc_utils as mu
import utils.poker_utils as pu


@mu.timer
def __main__():

    answer = 0
    count = 0

    project_root_dir = Path(__file__).parent.parent

    with open(project_root_dir / "data_items/54_hands.txt") as f:
        lines = f.readlines()
    
    for line in lines:
        card_strings = line.split(" ")
        card_strings[-1] = card_strings[-1].replace("\n","")

        cards = tuple(pu.Card.from_str(card_string) for card_string in card_strings)
        
        p1_hand = pu.Hand(cards[:5])
        p2_hand = pu.Hand(cards[5:])
        
        result = p1_hand.beats(p2_hand)

        if p1_hand.hand_rank.value > 1 or p1_hand.hand_rank.value > 1:
            print(p1_hand, p2_hand, p1_hand.hand_rank.name, p2_hand.hand_rank.name, result)
        count +=1 
        if result:
            answer += 1

    print(count)

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")