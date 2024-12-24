import math
from typing import List
import itertools

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
    if x == 1:
        return False

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

def get_base_2(x: int) -> str:

    highest_power_of_2_less_than_x = math.floor(math.log2(x))
    result = ["0"] * (highest_power_of_2_less_than_x + 1)

    target = x
    for idx, power in enumerate(reversed([2 ** n for n in range(highest_power_of_2_less_than_x + 1)])):
        
        if target - power >= 0:

            result[idx] = "1"

            if target == power:
                break

            target -= power

    result = "".join(result)

    return result

def is_palindrome(x: int = None, chars: List[str] = []):
    
    failed = False
    
    if x:
        chars = list(str(x))
    
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

def get_digits(x: int) -> List[str]:
    return [i for i in list(str(x))]

def get_pythagorean_triplets_up_to_x(x: int):

    squares = [i ** 2 for i in range(1, x + 1)]

    triplets = []
    for x, y in itertools.product(squares, squares):
        if abs(x - y) not in squares:
            continue
        triplet = {int(math.sqrt(x)), int(math.sqrt(y)), int(math.sqrt(abs(x-y)))}
        if triplet not in triplets:
            triplets.append(triplet)

    return triplets