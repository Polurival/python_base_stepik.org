import requests
import json

url = 'https://api.artsy.net/api/artists/'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTUwMDEyODYwMywiaWF0IjoxNDk5NTIzODAzLCJhdWQiOiI1OTYwZWFkYmM5ZGMyNDZlNDE2ZjM5MWQiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNTk2MGVhZGJjOWRjMjQ2ZTQxNmYzOTFlIn0.PX395mznnlp8hzRFZ786bbce23_E_8b7w-rWxC0TJKw'

# создаем заголовок, содержащий наш токен
headers = {'X-Xapp-Token' : token}

artists = {}
with open('dataset_24476_4.txt') as f, open('dataout4.txt', 'w', encoding='UTF-8') as outf:
    for artist_id in f.readlines():
        artist_id = artist_id.strip()

        # инициируем запрос с заголовком
        r = requests.get(url + artist_id, headers=headers)

        # разбираем ответ сервера
        j = json.loads(r.text)
        artists[j['sortable_name']] = j['birthday']
    print(artists)

    for name, birth in sorted(artists.items(), key=lambda x:(x[1], x[0])):
        outf.write(name + '\n')
        print(name, birth)