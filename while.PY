# 함수와 스코프

a = 3 # global a

def my_func():
	global a # 함수 정의
	a = 7 # local a
	print(a)

my_func(a) # 함수 호출 == [local a = 7, print(a)]
print(a)
