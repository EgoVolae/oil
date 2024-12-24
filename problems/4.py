import math
import numpy as np
from itertools import product

def is_palindrome(x: int):
    
    failed = False
    chars = str(x)
    if len(chars) % 2 == 0:
        for i in range(0, int(len(chars) / 2)):
            if chars[i] != chars[len(chars) - 1 - i]:
                failed = True
                break
    else:
        for i in range(0, int((len(chars) - 1) / 2)):
            if chars[i] != chars[len(chars) - 1 - i]:
                failed = True
                break

    return not(failed)

biggest_p = 0
for a, b in product(range(1000), range(1000)):
    c = a * b
    if is_palindrome(c):
        if c > biggest_p:
            biggest_p = c

print(biggest_p)