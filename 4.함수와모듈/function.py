# 함수의 정의
# def {function_name}({parameters}):
# 로 함수의 정의 시작
# 들여쓰기(indent)로 기존 코드와 구분됨
# 매개변수가 없을 경우, 생략 가능
# 반환값이 없을 경우, 생략 가능
# 함수의 정의로는 실제 명령문이 실행되지 않음
# 동일한 함수명으로 정의할 경우, 함수가 재정의 됨
# 함수는 반환되는 순간 종료됨 (return statement)

# 함수의 호출
# 정의된 함수를 실제로 사용
# function_name(arguments) 형태로 호출
# 매개변수(Parameter): 함수의 정의에 사용되는 변수명
# 인자(Argument): 함수의 호출 시 전달되는 실제 값
# 결과값을 변수에 저장할 수 있음

# 함수의 활용
# 코드 재사용성 증가
# 가독성 향상
# 유지 보수성 향상
# 재귀호출


# 함수의 정의
def func(name):
    print(f"This is Function. Hello {name}!")

# 함수의 호출
func("Cha")


# 반환값 사용하기
def sum(num1, num2):
    return num1 + num2
def div(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 / num2
result_sum = sum(6, 2)
result_div = div(3, 2)
print(result_sum)
print(result_div)


# 기본 매개변수 (Default Parameter)
# 함수를 호출할 때 매개변수를 제공하지 않으면, 자동으로 할당되는 값
# 함수를 유연하게 사용할 수 있음
# 매개변수 명 = 기본값 형태로 정의
# 기본 매개변수는 일반 매개변수 뒤에 위치

def study(name, language="python"):
    print(f"{name}님은 {language} 수업 중입니다.")
study("예원")

# 기본 매개변수 활용하기
# 매개변수 값을 전달하지 않으면 기본 매개변수가 사용됨
# 기본 매개변수 사용 시, 가변 객체(리스트, 딕셔너리 등)가 변조될 수 있음
# 가변 객체를 기본 매개변수로 사용할 경우, 함수 내부에서 생성하도록 구성

def process_data(data, options=None):
    if options is None:
        options = {
            "name": "Unknown"
        }
    
    # options 딕셔너리를 사용하여 데이터 처리 로직을 구현
    pass

# 키워드 인자 (Keyword Argument)
# 함수 호출 시 인자(Argument)와 매개변수(Parameter)는 위치에 의해 연결됨
# 위치 인자 (Positional Arguments)
# 키워드 인자: 함수 호출 시 인자에 매개변수 이름을 넣어 전달
# 인자와 매개변수의 열결을 명확히 보여줄 수 있음
# 매개변수의 순서에 영향을 받지 않으므로, 보다 유연하게 구성할 수 있음

# 키워드 인자 활용하기
# 키워드 인자와 위치 인자 혼용하여 사용
# 키워드 인자는 위치 인자 뒤에 위치해야 함
# 코드의 가독성을 향상시키고 함수 호출을 명확하게 함

def greet(name, greeting):
    print(greeting, name)

greet(name="Alice", greeting="hello")
greet(greeting="Hi", name="Bob")
greet("Bob","Hi")

# 가변 인자 리스트 (Arbitrary Argument List)
# 여러 인자를 유연하게 처리할 수 있게 활용
# 함수 정의에서 매개변수 이름 앞에 *을 붙여서 정의
# 튜플로 묶여서 전달 됨

def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result
total_number = add_numbers(1,2,3,4,5,6)
print(total_number)

# 가변 인자 리스트 활용하기
# 원하는 만큼의 인자를 전달할 수 있음
# 다른 매개변수와 함께 사용할 수 있으며, 일반 매개변수 뒤에 위치해야 함
# 하나만 정의 가능

add_numbers(1)
add_numbers(1, 10, -10, 5)

# 키워드 가변 인자 리스트 (Keyword Arguments List)
# 여러 인자를 유연하게 처리할 수 있게 활용
# 함수 정의에서 매개변수 이름 앞에 **을 붙여서 정의
# 딕셔너리로 묶여서 전달 됨

def print_kv(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 키워드 가변 인자 리스트 활용하기
# 원하는 만큼의 인자를 전달할 수 있음
# 매개변수 이름과 값을 직접 연결하여 호출 (매개변수명 = 값)
# 다른 매개변수와 함께 사용할 수 있으며, 모든 매개변수 중 가장 뒤에 위치해야 함

print_kv(name="alpha", age=10)
print_kv(name="beta", country="USA")
print_kv(key="name")

def display_info(name, *args, **kwargs):
    print("Name::", name)
    print("Known Languages::", ', '.join(args))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 변수의 생명주기
# 함수 내에서 변수를 정의하면, 함수 밖에서 사용할 수 있을까? NO    -> 지역변수
# 함수 밖에서 변수를 정의하면, 함수 내에서 사용할 수 있을까? YES   -> 전역변수(가장상위)

# 전역변수와 지역변수
# 전역변수: 가장 상위 코드블록에 정의된 변수 (또는 global 키워드를 사용하여 정의)
    # 프로그램 어디에서도 사용 가능
# 지역변수: 특정 함수 내에서 정의된 함수
    # 함수 내부에서만 접근 가능
    # 지역변수는 함수 호출이 완료되면 자동으로 소멸