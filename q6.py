users = {
	'total_user': 9,
	'information': [
			{'name': 'alex', 'age': 50, 'license':True},
			{'name': 'june', 'age': 44, 'license':False},
			{'name': 'peter', 'age': 17, 'license':False},
			{'name': 'bob', 'age':26, 'license':True},
			{'name': 'elle', 'age': 70, 'license':False},
			{'name': 'conny', 'age':5, 'license':False},
			{'name': 'jason', 'age':18, 'license':False},
			{'name': 'alison', 'age':36, 'license':True},
			{'name': 'joe', 'age':22, 'license':True},
	]
}
# 면허가 있는 인원들의 평균 나이를 구해주세요
license_cnt = 0
license_age = 0

a = users['information']
for i in a:
    if i['license'] == True:
        license_age += i['age']
        license_cnt += 1


print(license_age/license_cnt)

