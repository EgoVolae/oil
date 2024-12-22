import math
from typing import List

def get_biggest_prime_factor(x: int) -> int:
    """
    Returns the largest prime factor of x
    """

    if x in (2, 3):
        return x

    root = math.sqrt(x)
    biggest_int_lte_sqrt = math.floor(root)
    for i in reversed(range(2, biggest_int_lte_sqrt + 1)):

        if x % i != 0:
            continue
        if lazy_is_prime(i):
            return i
    
    ## If we get here, it means that x is prime
    return x


def lazy_is_prime(x: int) -> bool:
    """
    Returns a Boolean indicating whether or not x is prime
    """

    root = math.sqrt(x)
    for i in range(2, math.floor(root + 1)):
        if x % i == 0:
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
    biggest_int_lte_sqrt = math.floor(root)
    for i in reversed(range(1, biggest_int_lte_sqrt + 1)):

        if x / i != math.floor(x / i):
            continue
        q = math.floor(x / i)
        if i == q:
            to_ret.extend([i])
        else:
            to_ret.extend([i, q])
    
    if proper:
        to_ret = [y for y in to_ret if y != x]

    return to_ret

def get_prime_decomposition(x: int) -> List[int]:

    target = x
    prime_factors= []
    while target > 1:

        biggest_prime_factor = get_biggest_prime_factor(target)
        prime_factors.append(biggest_prime_factor)
        target = int(target / biggest_prime_factor)
    
    return sorted(prime_factors)