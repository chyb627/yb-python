# 조건문
value = 60

# 50보다 큰 경우 Great!, 20을 초과하는 경우, Big! 그렇지 않은 경우 Small!
if value > 50:
    print("Great!")
elif value > 20:
    print("Big!")
else:
    print("Small!")


# 날씨가 흐리고, 강수확률이 70% 이상이면 비가온다.
condition = "맑음"
rain_rate = 0.70

if condition == "흐림" and rain_rate >= 0.70:
    print("비가 올 확률이 높습니다.")
elif condition == "흐림":
    print("날씨가 많이 흐립니다.")
elif condition == "맑음" and rain_rate >= 0.70:
    print("맑지만 비가 올 확률이 높습니다.")
else:
    print("날씨가 좋습니다.")


# 사용자로부터 두개의 값을 입력받는다.
var1 = input("첫 번째 값을 입력해주세요: ")
var2 = input("두 번째 값을 입력해주세요: ")

# 입력값을 숫자로 변환
num_var1 = int(var1)
num_var2 = int(var2)

# 첫 번째 값이 크다면 "Win", 두 번째 값이 크다면 "Lose"를 출력한다.
# 두 값이 같다면, "Draw"를 출력한다.
if num_var1 > num_var2:
    print("Win")
elif num_var1 < num_var2:
    print("Lose")
else:
    print("Draw")


# 점수를 입력받는다.
score_str = input("점수를 입력해주세요: ")
score = int(score_str)

# 점수의 각 등급에 따른 결과를 출력한다. (A:90~99, B:80~89, C:70~79, D:60~69, F: ~59)
if score <= 99 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
elif score <= 69 and score >= 60:
    grade = "D"
elif score <= 59 and score >= 1:
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"등급은 {grade}입니다.")