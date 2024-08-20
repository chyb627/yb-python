# 빈 튜플 생성
# 변수를 정의할 때 값을 넣어줘야한다. 빈값 x
# append같은 함수를 사용할 수 없다.
# 하나의 값만 넣어줄땐 ,를 넣어서 이 내용이 튜플임을 알려줘야한다.
my_tuple = (1, ) 

# 과일 바구니
fruits = ("apple", "banana", "blueberry")
first = fruits[0]
print("first:", first)

# 패킹과 언패킹
tp = 1, 2, 3
print(tp) # 패킹
v1, v2, v3 = tp
print(f"{v1}, {v2}, {v3}") # 언패킹

a = 10
b = 20
# temp = a # a = 10, b = 20, temp = 10
# a = b    # a = 20, b = 20, temp = 10
# b = temp # a = 20, b = 20, temp = 10

a, b = b, a # (20, 10)을 언패킹해서 a와 b에 할당하겠다는 뜻
print("a:", a)


tp1 = (1, 2, 3, 4, 5, 6, 7, 8)
val1, val2, val3, *vals, _ = tp1
print(vals) # [4, 5, 6, 7] 튜플이 리스트로 저장된다.
vals.append(10) # 리스트이므로 append연산이 가능해진다.
print(vals) # [4, 5, 6, 7, 10]