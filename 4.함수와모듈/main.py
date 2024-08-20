
# 모듈이란?
# 파이썬 정의와 문장을 담고 있는 .py파일
# 함수, 변수, 클래스 등을 포함
# 모듈을 통해 코드를 구조화하고, 유지보수하기 용이해짐
# 작성된 모듈은 다른 프로그램에서 재사용 가능

# 모듈 사용하기
# 모듈 생성하기: .py 파일에 정의
# 모듈을 다른 프로그램에서 가져와 사용하기
    # import `모듈명`
    # 모듈 내에서 다른 모듈을 가져오는 것 또한 가능
# 모듈의 이름: __name__ 으로 참조 가능

import calc

print(calc.add(3, 4))
print(calc.sub(3, 4))
print(calc.div(3, 4))

# 모듈 가져오기 - 지역 네임스페이스(Namespace)
# 모듈을 지역 네임스페이스로 가져오기
    # from `모듈명` import `개체명`, `개체명2`
    # 이렇게 가져올 경우, 해당 개체 이름을 바로 사용할 수 있음
    # from `모듈명` import *
        # 모듈 내의 모든 개체를 import해올 수 있음(_로 시작하는 것 제외)
        # 의도와 다르게 모듈 내 모든 정보를 가져오기 때문에, 가급적 사용하지 말것

# 모듈 활용하기
# 모듈로서 코드와, 메인 프로그램으로서 코드를 어떻게 구분할 수 있을까?
# if __name__ == "__main__":
# 파이썬 인터프리터로 실행한 파일은 모듈명이 __main__으로 고정됨

# 패키지란?
# 모듈의 계층구조를 만드는 방법
# 모듈을 계층화하고, 모듈을 포함하는 디렉토리의 집합
# 디렉토리 구조를 활용하여 연관성 있는 모듈을 그룹화하고 정리할 수 있음
# 코도의 구조화와 재사용을 용이하게 만들며, 대규모 프로젝트에 필수적으로 사용됨

# 패키지의 구성
# 디렉토리 패키지 아래에 모듈들이 구성
# 서브패키지는 디렉토리 계층구조로 정의
# my_package/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#       __init__.py
#       module3.py

# 패키지 바깥에서 모듈 임포트하기: import package.module
    # 실제 모듈을 활용 시 : package.module.function()
# 별칭 이용하기: import package.module as alias
    # alias.function()
# 패키지 내의 모든 모듈 임포트하기: from package import *
    # 허용된 모듈만 import 가능

# __init__.py
# 이 디렉토리가 파이썬 패키지임을 알려주는 파일
# 패키지 수준에서 사용되는 변수, 함수, 또는 초기화 로직이 정의됨
# 하위 모듈을 미리 로드하거나, 전역변수를 정의하는 등
# __all__을 활용하여, 참조하게 만들 모듈만 선택 가능

# 패키지 내 특정 모듈만 사용
# from sound_system from *
# __init__.py(sound_system 패키지)
# __all__ = ["echo", "surround", "reverse"]
# def reverse(msg: str):
#   retrun msg[::-1]