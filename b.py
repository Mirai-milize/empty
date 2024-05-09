
users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}

# 평균 나이 구하기
# "sum" 변수명으로 쓰고 싶으면 acc를 쓰세요.
A = users['information']
i = 0
sm = 0

while i < int(len(A)) :
    sm += A[i]['age']
    i += 1

print(sm / int(len(A)))