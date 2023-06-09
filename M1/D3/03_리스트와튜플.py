#리스트와 튜플

#list
ls1 = [1,2,3,4,5]
print(ls1)

ls2 = [1, 'tt', True]
print(ls2)

# Empty list --> [] or list()

# range 사용해 리스트 만들기
print(list(range(10)))              # 0부터 시작
print(list(range(8, 14)))           # 시작점 지정
print(list(range(100, 1000, 100)))  # 증가폭 지정

# 튜플
tu1 = (1,2,3)
tu2 = 1, 2, 3
print(tu1, tu2)

tu3 = 'tt', 22, 22.334, False
print(tu3)

# range 사용해 튜플 만들기
print(tuple(range(100, 1000, 100)))

# 리스트와 튜플로 변수 만들기
l = [1, 2, 3]       #튜플도 가능
a, b, c = l
print(a, b, c)