# 문자열 변수 선언
str_var = "This is my python code."
multi_line = """I'm a developer.
I ues python.
Thank you."""
print(str_var)
print(multi_line)

# 문자열 더하기
inum1 = 12
inum2 = 34
snum1 = "12"
snum2 = "34"
print(inum1+inum2) # 46
print(snum1+snum2) # 1234
print(snum1*3) # 121212

# 인덱싱
print(str_var[11]) # p
print(str_var[-1]) # .
print(str_var[-5]) # c

# 슬라이싱
print(str_var[11:17]) # python
print(str_var[11:-6]) # python
print(str_var[:10]) # This is my

print(str_var.isalpha()) # False, space(공백) 및 .(마침표)는 알파벳이 아니므로 False
print(str_var.upper()) # THIS IS MY PYTHON CODE.
print(str_var.swapcase()) # tHIS IS MY PYTHON CODE. 소문자->대문자, 대문자->소문자 바꿔주는 함수.
print(str_var.replace("my", "your")) # 현재 문자열에 있는 my를 your로 바꿈

# Format String
weather = "흐림"
temp = 15.8

# % code (%s, %d, %f)
res = "[%s / %f도] 오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp, weather, temp)
print(res)

# .format()
res2 = "오늘 날씨는 {} 입니다. 기온은 {}도 입니다.".format(weather, temp)
res3 = "오늘 날씨는 {1} 입니다. 기온은 {0}도 입니다.".format(weather, temp)
print(res2)
print(res3)

# f"" 
# f리터럴
res4 = f"오늘 날씨는 {weather}입니다. 기온은 {temp}도 입니다."
print(res4)

# 사용자로부터 문자열 입력받기
print("숫자를 입력해주세요.")
inp = input()
print(inp)
num = int(inp) + 1
print(f"입력받은 값에 1을 더하면, {num} 입니다.")