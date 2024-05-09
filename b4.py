# 리스트 컴프리헨션
users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

a = users['information']
b = [i['name'] for i in a if i['license'] == False]

print(b)