def solution(my_string):
    a = list(my_string)
    b = []
    for i in a:
        if type(i) == type(1):
            b.append(i)
    return sum(b)

print(solution('h1k3n4k5'))