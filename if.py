age = int(input())

if age >= 20:
    if age >= 30:
        print('30대')
    else:
        print('20대')

else:
    if age >= 10:
        print('청소년')
    elif age >= 5:
        print('어린이')
    else:
        print('영유아')