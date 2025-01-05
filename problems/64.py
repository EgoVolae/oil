import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple, Set
import math
from tabulate import tabulate
import itertools
import numpy as np

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


class RadicalFraction:

    a: int
    b: int
    c: int
    d: int
    x: int

    def __init__(self, a, b, c, d, x) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x
    
    def cancel(self) -> "RadicalFraction":

        if self.c != 0:
            return self
        
        gcd = math.gcd(self.a, self.b, self.d)

        if gcd == 1:
            return self
        
        return RadicalFraction(int(self.a / gcd), int(self.b / gcd), self.c, int(self.d / gcd), self.x)

    def transform(self) -> "RadicalFraction":
        return RadicalFraction(self.b * self.c, self.a * self.x * (self.c - self.d) - self.b * self.d, 0, self.x * self.c ** 2 - self.d ** 2, self.x)

    @property
    def numerator_value(self) -> float:
        return (self.a * math.sqrt(self.x) + self.b)
    
    @property
    def denominator_value(self) -> float:
        return (self.c * math.sqrt(self.x) + self.d)

    @property
    def value(self) -> float:
        return self.numerator_value / self.denominator_value

    @property
    def floor(self) -> int:
        return math.floor(self.value)

    @property
    def reciprocal(self) -> "RadicalFraction":
        return RadicalFraction(self.c, self.d, self.a, self.b, self.x)

    def to_integer_and_fraction(self) -> Tuple:

        if self.c != 0:
            print(f"Needs to be transformed")
            raise Exception
        
        integer = self.floor

        fraction = RadicalFraction(self.a, self.b - self.floor * self.d, self.c, self.d, self.x)
        return (integer, fraction)

    def __str__(self) -> str:
        return f"({self.a}*sqrt({self.x}) + {self.b})/({self.c}*sqrt({self.x}) + {self.d})"

    def __eq__(self, other) -> bool:
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d and self.x == other.x


@mu.timer
def __main__():

    answer = 1  # We know that 2 has an odd period, and the code below doesn't work for 2, so we start at 3

    for x in range(3, 10_001):

        if int(math.sqrt(x)) == math.sqrt(x):
            continue

        integers = []
        target_frac = RadicalFraction(1, 0, 0, 1, x)
        seen_fracs = [target_frac]

        while True:

            integer, fraction = target_frac.to_integer_and_fraction()
            recip = fraction.reciprocal
            transformed_frac = recip.transform()
            cancelled_frac = transformed_frac.cancel()
            target_frac = cancelled_frac

            integers.append(integer)

            if target_frac in seen_fracs:
                break

            seen_fracs.append(target_frac)

        period = len(integers) - 1

        print(f"{x=}, {period=}, {integers=}")

        if period % 2 == 1:
            answer += 1

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")