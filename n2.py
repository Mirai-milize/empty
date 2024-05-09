arr = ['a', 'b', 'c']
check = [0] * 3
sel = [0] * 3

def perm(depth):
    if depth == 3:
        print(*sel)
        return
    
for i in range(3):
    if not check[i]:
        check[i] = 1
        sel[depth] = arr[i]
        perm(depth+1)
        check[i] = 0

perm(0)

