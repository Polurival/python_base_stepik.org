import requests

url = 'http://numbersapi.com/'
path = '/math'
params = {
    'json': 'true'
}

with open('dataset_24476_3.txt') as f, open('dataout.txt', 'w') as outf:
    for line in f.readlines():
        line = line.strip()
        res = requests.get(url + line + path, params=params)
        print(res.json()['text'])
        if res.json()['found']:
            outf.write('Interesting\n')
        else:
            outf.write('Boring\n')
