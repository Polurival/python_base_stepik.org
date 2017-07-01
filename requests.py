import requests
with open('dataset_3378_2.txt') as inf:
	url = inf.readline().strip()
print(url)
resp = requests.get(url)
print(resp.text)