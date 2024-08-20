# 예외처리
# 프로그램 실행 중 발생할 수 있는 예외(오류) 상황을 처리하는 매커니즘
# 프로그램의 비정상 종료를 막고, 예외 상황에 대한 적절한 조치를 취할 수 있음
# 의도된 예외 발생 및 처리를 통해, 프로그램이 목적에 맞게 동작하도록 구현

try:
    value = int("abc") # 예외가 일어날 수 있는 코드
except ValueError:
    print("숫자로 변환할 수 없는 문자열입니다.") # 예외가 일어나면 실행될 코드
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except:
    print("알 수 없는 오류입니다.")
else:
    print("변환이 완료되었습니다.") # 예외가 없을 때 실행될 코드
finally:
    print("프로그램을 종료합니다.") # 예외 발생 여부와 무관하게 마지막에 실행될 코드


# 예외처리 실습

while True:
    try:
        num1 = int(input("첫 번째 숫자를 입력해주세요. "))
        num2 = int(input("두 번째 숫자를 입력해주세요. "))
        result = num1 / num2
        print(f"나누기 결과는 {result} 입니다.")
        break
    except ValueError:
        print(f"정상적인 숫자를 입력해주세요.")
        continue
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        continue
    except:
        pass