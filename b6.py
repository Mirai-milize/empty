nums = [8, 4, 9, 7,6, 1, 5, 10]

# max 구현

min_num = 11
for i in nums:
    if min_num > i:
        min_num = i 
    
print(min_num)