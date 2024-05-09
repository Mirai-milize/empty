a = [1]

while a[-1] < 10:
    a.append(a[-1]+1)

print(sum(a))

