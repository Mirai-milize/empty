# a = [[15,2], [10,4], [5,6], [7,8]]

# b = sorted(a, key=lambda x: -x[0])
# print(b)

dict = { 1: 'd', 2: 'c', 3: 'a', 4: 'b'}

dict[5] = 'e'

srt_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(srt_dict)

