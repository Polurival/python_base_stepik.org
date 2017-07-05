# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова,
# состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.sub(r'\b[aA]+\b', 'argh', line, 1)
    if has_two_cat is not None:
        print(has_two_cat)