# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.search(r'.*\\.*', line)
    if has_two_cat is not None:
        print(line)