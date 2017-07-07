import requests_example0
with open('dataset_3378_2.txt') as inf:
	url = inf.readline().strip()
print(url)
resp = requests_example0.get(url)
print(resp.text)