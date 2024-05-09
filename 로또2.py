import random

def lotto(N):
    lucky = [11, 13, 14, 15, 16, 45]
    lucky_nums = set(lucky)
    lotto_range = list(range(1, 46))
    cnt = {i:0 for i in range(7)}

    for _ in range(N):
        a = random.sample(lotto_range, 6)
        hit = len(lucky_nums & set(a))
        cnt[hit] += 1

    return cnt    

