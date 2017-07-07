import requests
import re

link = input()

res = requests.get(link)

links = re.findall(r'(?:<a.*href[\s]*=[\s]*(["\']|["\'][a-z]*://))([a-z0-9]+([\-\.]{1}[_a-z0-9]+)*\.[a-z]{2,5})',
                   res.text)

domains = set()
for groups in links:
    domains.add(groups[1])

sorted_domains = sorted(domains)
for domain in sorted_domains:
    print(domain)
