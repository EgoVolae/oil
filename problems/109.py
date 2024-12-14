# For each figure we essentially need to break it down into the number of ways
# we can get integers to sum to it
# Then the even numbers to go on the end as potential doubles

# Need a function that takes a natural number and gives a list of all
# integers that sum to it

from typing import Dict, List, Tuple
import math
from dataclasses import dataclass

@dataclass
class SDT:
    x: int
    S: int
    D: int
    T: int

    @property
    def S_rep(self) -> str:
        if self.S == 0:
            return ""
        return f"{self.x}S"

    @property
    def D_rep(self) -> str:
        if self.D == 0:
            return ""
        return f"{int(self.x / 2)}D"

    @property
    def T_rep(self) -> str:
        if self.T == 0:
            return ""
        return f"{int(self.x / 3)}T"
        
    @property
    def F(self) -> int:
        return self.S + self.D + self.T
    
    @property
    def empty(self) -> bool:
        return self.S + self.D + self.T == 0


def get_breakdowns_for_n(n: int, breakdowns_cached) -> List[List[int]]:

    if n == 1:
        return [[1]]

    result = [[n]]
    for i in range(1, n):
        if breakdowns_cached.get(n-i) is not None:
            smaller_breakdowns = breakdowns_cached[n-i]
        else:
            smaller_breakdowns = get_breakdowns_for_n(n - i, breakdowns_cached)
            breakdowns_cached[n-i] = smaller_breakdowns
        beefed_breakdowns = [p + [i] for p in smaller_breakdowns if len(p) < 3]
        beefed_breakdowns = [sorted(x) for x in beefed_breakdowns]
        
        result.extend(beefed_breakdowns)
    return result


def get_breakdowns_up_to_n(n) -> Dict[int, List[List[int]]]:

    breakdowns_cached = {}
    get_breakdowns_for_n(n + 1, breakdowns_cached)
    return breakdowns_cached

def x_to_SDT(x: int) -> SDT:

    S, D, T = 0, 0, 0
    if x <= 20 or x == 25:
        S = 1
    if (x % 2 == 0 and x / 2 <= 20) or x == 50:
        D = 1
    if (x % 3 == 0 and x / 3 <= 20):
        T = 1
    
    return SDT(x, S, D, T)

def get_checkouts_for_breakdown(breakdown: Tuple[int]) -> List:

    SDT_representation: List[SDT] = [x_to_SDT(x) for x in breakdown]
    breakdown_to_SDT = {x: x_to_SDT(x) for x in breakdown}

    if len(SDT_representation) == 1:
        return [SDT_representation[0].D_rep]
    
    to_ret = list()

    for SDT in SDT_representation:

        if SDT.D == 0:
            continue

        other_elements = [other_SDT for other_SDT in SDT_representation if other_SDT.x != SDT.x]
        # other_elements = {y: SDT for y, SDT in breakdown_to_SDT.items() if y != x}
        if len(set(other_elements)) == 1:

            other_elements_F = other_elements[0].F
            if other_elements_F == 1:
                to_ret.extend([None])
            if other_elements_F == 2:
                to_ret.extend([None]*3)
            if other_elements_F == 3:
                to_ret.extend([None]*6)
        
        else:
            num_checkouts = math.prod([SDT.F for SDT in other_elements])
            to_ret.extend([None] * num_checkouts)
    
    return to_ret

def get_checkouts_for_target(target: int) -> int:

    breakdowns = get_breakdowns_for_n(target, {})
    unique_breakdowns = set([tuple(ls) for ls in breakdowns])
    not_all_odd_breakdowns = []
    for breakdown in unique_breakdowns:
        if sum([x % 2 for x in breakdown]) == len(breakdown):
            continue  # We need at least one element to be even
        not_all_odd_breakdowns.append(breakdown)
    valid_breakdowns = []
    for breakdown in not_all_odd_breakdowns:
        SDT_representation: List[SDT] = [x_to_SDT(x) for x in breakdown]
        if any([SDT.empty for SDT in SDT_representation]):
            continue
        valid_breakdowns.append(breakdown)

    checkouts_for_target = list()
    for breakdown in valid_breakdowns:
        checkouts_for_breakdown = get_checkouts_for_breakdown(breakdown)
        checkouts_for_target.extend(checkouts_for_breakdown)
    return checkouts_for_target


highest_target_to_check = 10

total_checkouts = list()
for target in range(1, highest_target_to_check + 1):
    checkouts_for_target = get_checkouts_for_target(target)
    total_checkouts.extend(checkouts_for_target)
    print(f"{target}: {len(checkouts_for_target)} checkouts")

print(f"Total checkouts: {len(total_checkouts)}") 