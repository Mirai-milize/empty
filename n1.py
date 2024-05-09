from itertools import permutations, combinations

arr = ['a', 'b', 'c']

# print(list(permutations(arr,3)))

for i in permutations(arr, 3):
    print(*i)

for j in combinations(arr, 2):
    print(*j)

    