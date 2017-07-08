import requests
import re

a = input()
b = input()

res1 = requests.get(a)
links1 = re.findall(r'http.*html', res1.text)

answer = 'No'
for link1 in links1:
    try:
        res2 = requests.get(link1)
        links2 = re.findall(r'http.*html', res2.text)

        for link2 in links2:
            if b == link2:
                answer = 'Yes'
    except IOError as detail:
        continue
print(answer)
