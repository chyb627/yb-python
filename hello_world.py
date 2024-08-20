print('Hello world')

# 라이브러리
# 여러모듈과 패키지의 모음
# 특정 작업을 수행하기 위한 함수, 클래스, 상수 등의 모음
# 라이브러리는 여러 패키지들의 묶음으로 구성되며, 패키지는 여러 모듈의 묶음으로 구성
# 표준 라이브러리(Standard Library): 파이썬 설치 시 기본으로 제공됨
# 외부 라이브러리(Third-party Library): 다양한 회사, 개발자들이 제작하여 제공

# 파이썬 표준 라이브러리 활용하기
# 랜덤 숫자 생성하는 라이브러리: random
# 복잡한 수학 관련 라이브러리: math
# 시간과 날짜 라이브러리: datetime
# 파일, 디렉토리 등 운영체제 라이브러리: os

# import math
# result = math.sqrt(25)
# print("제곱근:", result)

# import datetime
# result = datetime.date.today()
# print("오늘의 날짜:", today)

# 파이썬 외부 라이브러리 활용하기
# 필요한 라이브러리 설치하기: pip (Package Installer for Python)
# python -m pip install {package_name}
# python -m pip install SomePackage==1.0.4 # specific version
# python -m pip install "SomePackage>=1.0.4" # minimum version

# 라이브러리 버전 관리하기: requirements.txt
# 어떤 라이브러리와 버전을 사용하는지 정확히 설정
# 외부 라이브러리의 업데이트에 우리 프로젝트가 영향을 받지 않도록

# 라이브러리 사용하기
# import {library_name}

# 기본설치: 모든 개발환경에 공통적으로 설치됨
# 가상환경: 해당 프로젝트에서만 사용되는 패키지 설치 (여러 프로젝트를 동시에 개발할 때, 의존성 충돌을 막을 수 있음)
