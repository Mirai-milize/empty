# 라이센스 있는 인원

users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

a = users['information']
b = 0
for i in a:
    if i['license'] == True:
        b += 1

print(b)
