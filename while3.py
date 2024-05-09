# 1 ~ 1000까지 3의 배수의 합은 얼마일까?

turn = 0
anwser = 0

while turn < 1000:
    turn += 1
    if turn % 3 == 0:
        anwser = anwser + turn

print(anwser)


