users = {
	'total_user': 9,
	'information': [
			{'name': 'alex', 'math': 50, 'science': 80},
			{'name': 'june', 'math': 44, 'science': 68},
			{'name': 'peter', 'math': 17, 'science': 90},
			{'name': 'bob', 'math':26, 'science': 100},
			{'name': 'elle', 'math': 70, 'science': 77},
			{'name': 'conny', 'math':5, 'science': 15},
			{'name': 'jason', 'math':18, 'science': 26},
			{'name': 'alison', 'math':100, 'science': 86},
			{'name': 'joe', 'math':22, 'science': 40},
	]
}

a = users['information']

# 1. 수학 점수가 가장 높은 사람의 이름을 구해주세요.
max_math = 0
math_name = {}
for i in a:
    if i['math'] > max_math:
        max_math = i['math']
        math_name = i
print(math_name['name'])

# 2. 수학 점수와 과학 점수의 합산이 가장 높은 사람을 구해주세요.

max_ms = 0
max_mxname = {}
for j in a:
    ma = j['math'] + j['science']
    if ma > max_ms:
        max_ms = ma
        max_mxname = j

print(max_mxname['name'])

# 정연님 좋은 코드

# answer = {'name': "", 'score_add': 0}

# for i in users['information']:
#     if i['math'] + i['science'] < answer['score_add']:
#         answer['name'] = i['name']
#         first['score_add'] = i['math'] + i['science']
    
# print(answer['name'])