py_res = {}
popular_list = {}

for n in range(1,11):
    infos = {
        'api_key': f'{API_KEY}',
        'language': 'ko',
        'page': n
    }
    res = requests.get(URL+path, params=infos)
    py_res = res.json()
    
    for movie in py_res['results']:
        if float(movie['vote_average']) > 8.0:
            popular_list[movie['title']] = movie['vote_average']

popular_list = sorted(popular_list.items(), key=lambda x: -x[1])

print(*popular_list[0:3])