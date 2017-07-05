# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.search(r'.*(cat).*(cat).*', line)
    if has_two_cat is not None:
        print(line)



