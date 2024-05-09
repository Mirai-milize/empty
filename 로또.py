import random

num = list(range(1, 46))
g = ['A', 'B', 'C', 'D', 'E']


for i in range(5):
    a = random.sample(num, 6)
    a.sort()
    print(g[i], end=' ')
    print('자동', *a)
    


 