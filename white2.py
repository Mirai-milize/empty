# 이름이 3글자인 사람의 명수

names = ['김철수','나얼','신짱구','원장','신형만','유리','맹구']

men = 0

for i in names:
    if len(i) == 3:
        men += 1

print(men)

