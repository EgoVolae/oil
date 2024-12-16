import math
from typing import List

def get_biggest_prime_factor(x: int) -> int:
    """
    Returns the largest prime factor of x
    """

    root = math.sqrt(x)
    biggest_int_less_than_root = math.floor(root)
    for i in reversed(range(2, biggest_int_less_than_root)):

        if x / i != math.floor(x / i):
            continue
        if lazy_is_prime(i):
            print(i)
            return i


def lazy_is_prime(x: int) -> bool:
    """
    Returns a Boolean indicating whether or not x is prime
    """

    root = math.sqrt(x)
    for i in range(2, math.floor(root + 1)):
        if x / i == math.floor (x / i):
            return False
    return True


def get_list_of_primes(n: int) -> List[int]:
    """
    Returns a list of the first n primes
    """

    if n == 0:
        return []
    
    if n == 1:
        return [2]
    
    result = [2]
    target = 3
    while len(result) < n:

        if lazy_is_prime(target):
            result.append(target)
        target += 1
    
    return result


def get_all_primes_up_to(n: int) -> List[int]:
    """
    Returns a list of all the primes up to n
    """

    result = []
    for i in range(2, n+1):
        if lazy_is_prime(i):
            result.append(i)
    return result


def get_all_factors(x: int, proper=False) -> List[int]:
    """
    Returns a list of all factors of an integer
    """

    if x == 1 or x == 0:
        return []

    to_ret = []
    root = math.sqrt(x)
    biggest_int_less_than_root = math.floor(root)
    for i in reversed(range(1, biggest_int_less_than_root)):

        if x / i != math.floor(x / i):
            continue
        q = math.floor(x / i)
        to_ret.extend([i, q])
    
    if proper:
        to_ret = [y for y in to_ret if y != x]

    return to_ret



