a = [0]

for _ in range(10): 
    if a[-1] <= 10:
        a.append(a[-1]+1)

print(sum (a))
print (a)