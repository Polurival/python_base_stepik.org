# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w﻿.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line)
    if has_two_cat is not None:
        print(has_two_cat)