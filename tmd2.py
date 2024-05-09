import requests
import pprint

API_KEY = 'd007df33e3f03e1148dcaee79c3de63c'
URL ='https://api.themoviedb.org/3'
path = '/movie/popular'

data = []
over_8 = []
name_vote = []


for n in range(1,11):
    infos = {
    'api_key': f'{API_KEY}',
    'language': 'ko',
    'page': n
    }
    res = requests.get(URL+path, params=infos)
    py_res = res.json()
    if n == 1:
        data = py_res['results']
    else:
        data += py_res['results']
    

for i in range(len(data)):
    if data[i]['vote_average'] >= 8:
        over_8.append(data[i])

for j in range(len(over_8)):
    name_vote.append([over_8[j]['title'], over_8[j]['vote_average']])

name_vote.sort(key=lambda x: -x[1])

for nums in range(3):
    print(name_vote[nums][0], name_vote[nums][1])
