black_list = [77, 3, 5, 9, 11, 25]
customers = [8, 1, 4, 6]

for customer in customers:
    if customer in black_list:
        break
    print(f'{customer}번 고객님 환영합니다.')
else:    # for - break -> else (for - else는 완주 축하 같은 형태)
    print('블랙리스트 고객이 감지되었습니다.')

