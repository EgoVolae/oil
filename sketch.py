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

a = mnt.totient_inc_exc(7026037)
b = mnt.totient(223344)
print(a)
print(b)

c = mnt.get_all_primes_up_to(math.floor(math.sqrt(10_000_000)))
print(len(c))