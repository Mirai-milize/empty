nums = [1, 1, 2, 3, 1, 4, 2, 3, 1, 2]
cnt = {}
for num in nums:
    cnt[num] = cnt.get(num, 0)+1
    # if cnt.get(num, -1) == -1:
    #     cnt[num] = 1
    # else:
    #     cnt[num] += 1

print(cnt)