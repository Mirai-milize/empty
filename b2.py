
users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

# 라이센스 없는 인원 이름

a = users['information']
b = []

for i in a:
    if i['license'] == False:
        b.append(i['name'])

print(b)
