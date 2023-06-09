# bool, 비교, 논리 연산자

# bool --> boolean 참과 거짓으로 구성되어있음
# 두 값의 관계 --> 비교 혹은 논리 연산자 사용

print(True, False)
print(int(True), int(False)) # 1, 0
print(bool(4)) # 0 아니면 다 True

# 등호 -> 같다 다르다
print('10 == 10 is', 10 == 10)
print('10 == 5 is', 10 == 5)
print('10 != 5 is', 10 != 5)

# 부등호 -> 작다 같다 크다
print('10 > 5 is', 10 > 5)
print('10 < 5 is', 10 < 5)

# 객체 비교
# is, not -> 연산자
print("1 == 1.0 is", 1.0 == 1)
print("1 is 1.0 is", 1.0 is 1) # 타입이 다르다
print("1 is not 1.0 is", 1.0 is not 1)

# 논리 연산자
# and, or, not
print(1 and 1, 1 and 0, 0 and 0)
print(1 or 1, 1 or 0, 0 or 0)
print(not 1, not 0)
# 우선순위: not > and > or
print(not 1 and not 0 or 1)

# 논리 + 비교 연산자
# 비교 연산자 우선 순위가 더 높다
print(10 > 5 or 5 < 10)

# 정수, 실수, 문자열을 bool로 판별하기
print(bool(1.5))        #True
print(bool(0.0))        #False
print(bool("Hey"))      #True
print(bool(""))         #False
print(bool(" "))        #True