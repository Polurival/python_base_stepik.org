# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
# Примечание:
# Для работы со словами используйте группы символов \b и \B.
# Описание этих групп вы можете найти в документации https://docs.python.org/3.5/library/re.html.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    has_two_cat = re.search(r'\bcat\b', line)
    if has_two_cat is not None:
        print(line)