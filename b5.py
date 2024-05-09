gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0}

# 반복문 집계/카빙하는 방식.

for i in gems:
    if i == 1:
        grades[1] += 1
    
    elif i == 2:
        grades[2] += 1

    else:
        grades[3] += 1

print(grades)

## 리스트 카운팅

gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0}

grades[1] = gems.count(1)
grades[2] = gems.count(2)
grades[3] = gems.count(3)

print(grades)

# 좋은 코드 (진호님)

gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {}

for i in gems:
    if i not in grades:
        grades[i] = 1
    else:
        grades[i] += 1

print(grades)
