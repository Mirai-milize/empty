arr = [i for i in range(25)]

a = arr.index(15)
print(a)
print(arr[a])
print(abs(arr[a-1]-arr[a+1]))