#1부터 100까지 더하는 코드?

a = [0]

for _ in range(100): # 반복문의 횟수 설정.
    if a[-1] <= 100:
        a.append(a[-1]+1)

print(sum (a))

# 더 쉬운 코드?

print(sum(list(range(1,10))))
print(sum(range(1, 11)))