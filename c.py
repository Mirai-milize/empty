a = [1,3,5,2,4,0] # 리스트는 수정가능, 반복가능 (iterable mutable)
a.sort()
print(a)

a[0] = 'b'
print(a)

a.pop(0)
print(a)

a.insert(0, 0)
print(a)

b = 'special' # 스트링은 수정불가능, 반복가능 (iterable imutable)
print(b[0])

# 리스트 하드코딩은 id값이 별개, 리스트 덧셈도 id가 별개로 생성 됨.



