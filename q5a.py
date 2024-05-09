gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {} # {3: 5, 1: 2, 2: 3}

# gems 리스트와 grades 집계 딕셔너리가 주어졌을 때,
# 가장 많이 채굴된 광물의 등급을 출력하시오.

for gem in gems:
    if gem not in grades:
        grades[gem] = 1
    else:
        grades[gem] += 1

most_gem = 0
most_grade = 0
for key, value in grades.items():
    if most_gem < value:
        most_gem = value
        most_grade = key
        
print(most_grade)
