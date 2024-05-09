# <수 정렬하기>
# 주어진 2차원 리스트를 기준에 따라서 정렬하시오.
# [앞쪽, 뒤쪽] 이라고 할 때, 뒤쪽이 '작은' 순서로 정렬하되 만약 같다면 앞쪽이 '큰' 순서대로 정렬하시오.
nums = [[70, 30], [70, 10], [20, 30], [50, 90], [40, 80], [80, 90], [10, 60]]

nums.sort(key=lambda x: (x[1], -x[0]))

print(nums)