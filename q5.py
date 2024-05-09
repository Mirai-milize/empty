gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {}

# gems 리스트와 grades 집계 딕셔너리가 주어졌을 때,
# 가장 많이 채굴된 광물의 등급을 출력하시오.

for i in gems:
    if i not in grades:
        grades[i] = 1
    
    else:
        grades[i] += 1

max_grade = 0
max_count = 0
for j in grades:
    if grades[j] > max_count:
        max_count = grades[j]
        max_grade = j

print(max_count)
print(max_grade)
