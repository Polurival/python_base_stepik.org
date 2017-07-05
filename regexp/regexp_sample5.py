# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
# output:
# blabla is a tandem repetition
# 123123 is good too

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.search(r'\b(.+)\1\b', line)
    if has_two_cat is not None:
        print(line)