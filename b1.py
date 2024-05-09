users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

names = []

A = users['information']
i = 0 

while i < int(len(A)):
    names.append(A[i]['name'])
    i += 1

print(names)