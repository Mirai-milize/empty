import requests  # 모듈 import
import pprint  # 출력 형식 조정 내장 모듈 'Pretty Print'

API_KEY = 'd007df33e3f03e1148dcaee79c3de63c'  # API Key
URL = 'https://api.themoviedb.org/3'  # Base URL
path = '/movie/popular'  # 인기 영화

# 딕셔너리로 구조화 된 부가 정보들 
infos = {
    'api_key': f'{API_KEY}',
    'language': 'ko',
    'page': 1
}

res = requests.get(URL+path, params=infos)  # get 메서드 안 인자로 전달
py_res = res.json()  # 파이썬 파싱
pprint.pprint(py_res)  # 최종 결과