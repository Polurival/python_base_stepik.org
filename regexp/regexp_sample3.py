# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.search(r'.*z.{3}z.*', line)
    if has_two_cat is not None:
        print(line)