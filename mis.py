# 우수 고객, 일반 고객 나눠서 판별해보자!

buy = int(input('구매수량을 입력해주세요 : '))
cost = int(input('구매금액을 입력해주세요 : '))
print()

nbuy = 10 - buy
ncost = 1000 - cost

if buy < 0 or cost < 0:
    print('올바른 수량을 입력해주세요.')

elif buy >= 10 and cost >= 1000:
    print('고객님의 등급은 vip등급입니다.')

elif buy >= 10 or cost >= 1000:
    print('고객님의 등급은 우수고객입니다.')

    if buy >= 10 and cost <= 1000:
        print(f'vip 등급까지 "{ncost}"만큼의 추가금액이 필요합니다.')
    
    else:
        print(f'vip 등급까지 "{nbuy}"만큼의 구매수량이 필요합니다.')

else:
    print('고객님의 등급은 일반고객입니다.')
    print(f'vip등급이 되시려면 "{ncost}"의 추가금액과 "{nbuy}"구매수량이 필요합니다.')

