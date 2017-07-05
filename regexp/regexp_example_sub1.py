# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.sub(r'human', 'computer', line)
    if has_two_cat is not None:
        print(has_two_cat)