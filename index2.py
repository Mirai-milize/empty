# 다음과 같은 api 데이터가 있을 때, 학생들의 데이터를 전처리하여,
# 우선 과학 점수가 '높은' 순으로, 만약 과학 점수가 같다면 수학 점수가 '낮은' 순서대로 학생 이름을 출력하시오.
users = {
	'total_user': 9,
	'information': [
			{'name': 'alex', 'math': 50, 'science': 80},
			{'name': 'june', 'math': 44, 'science': 40},
			{'name': 'peter', 'math': 17, 'science': 90},
			{'name': 'bob', 'math':26, 'science': 100},
			{'name': 'elle', 'math': 70, 'science': 77},
			{'name': 'conny', 'math':5, 'science': 15},
			{'name': 'jason', 'math':18, 'science': 15},
			{'name': 'alison', 'math':100, 'science': 90},
			{'name': 'joe', 'math':22, 'science': 40},
	]
}

lst_inform = users['information']

lst_inform.sort(key=lambda x: (-x['science'], x['math']))
print(lst_inform)
def name():
    for i in range(len(lst_inform)):
        print(lst_inform[i]['name'])

name()
