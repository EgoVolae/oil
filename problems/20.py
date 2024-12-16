import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors


a = math.factorial(100)
result = 0
for char in str(a):
    result += int(char)
print(result)