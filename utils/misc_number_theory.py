import math
from typing import Callable, Dict, List, Tuple
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


def get_all_factors(x: int, proper=False, asc=False) -> List[int]:
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

    if asc:
        to_ret = sorted(to_ret)

    return to_ret

def get_prime_decomposition(x: int) -> List[int]:

    target = x
    prime_factors= []
    while target > 1:

        biggest_prime_factor = get_biggest_prime_factor(target)
        prime_factors.append(biggest_prime_factor)
        target = int(target / biggest_prime_factor)
    
    return sorted(prime_factors)

def get_next_prime(x: int) -> str:
    
    target = x + 1
    while True:
        if lazy_is_prime(target):
            return target
        target += 1

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

def get_first_m_continued_fractions(m: int, b_gen_func: Callable) -> Tuple[Tuple, Tuple]:

    """
    Returns two tuples:
    [A_0, A_1, A_2, ..., A_{m-1}]
    [B_0, B_1, B_2, ..., B_{m-1}]
    , where A_{m-1}/B_{m-1} is the mth continued fraction where the b terms are given by b_gen_func
    
    """

    b_0, b_1 = b_gen_func(0), b_gen_func(1)

    A_series = [b_0, b_0 * b_1 + 1]
    B_series = [1, b_1]
    b_series = [b_0, b_1]
    n = 2
    while n < m:
        
        A_n_minus_1 = A_series[n - 1]
        A_n_minus_2 = A_series[n - 2]
        B_n_minus_1 = B_series[n - 1]
        B_n_minus_2 = B_series[n - 2]

        b_n = b_gen_func(n)

        A_n = b_n * A_n_minus_1 + A_n_minus_2
        B_n = b_n * B_n_minus_1 + B_n_minus_2

        A_series.append(A_n)
        B_series.append(B_n)
        b_series.append(b_n)

        n += 1
    
    return tuple(A_series), tuple(B_series)

def is_perfect_square(x: int) -> bool:
    return math.sqrt(x) == int(math.sqrt(x))

def is_integer(x) -> bool:
    return math.floor(x) == int(x)

def are_coprime(x: int, y: int) -> bool:
    return math.gcd(x, y) == 1

def totient(x: int) -> int:
    """
    Returns the totient of x
    """
    if x == 1:
        return 1

    prime_decomposition = get_prime_decomposition(x)
    result = x
    for prime in set(prime_decomposition):
        result *= (1 - 1 / prime)

    return int(result)


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

