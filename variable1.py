# 변수의 선언
var = 42
print(var)  # 42
print(var+10)  # 더하기 52
print(var-10)  # 빼기 32
print(var/10)  # 나누기 4.2
print(var//10)  # 몫 4
print(var%10)  # 나머지 2

var2 = var/10
print(var>var2) # True

result1 = var * 10 + 5 # 425
result2 = 5 + var * 10 # 425
result3 = (5 + var) * 10 # 470
print(result1, result2, result3)

is_true = True
is_false = False
print(is_true and is_true) # True
print(is_true and is_false) # False
print(is_false and is_false) # False
print(is_true or is_false) # True