# yb-python
python 기초 공부

## 파이썬 명령어
```sh
# version확인
python --version

# pythone IDLE 접속
python

# hello_world.py 파일 실행
$ python hello_world.py
```

## 파이썬 가상환경

```sh
# 가상환경 생성
$ python -m venv cha

# 가상환경 활성화 (mac/linux)
$ source cha/bin/activate

# 가상환경에서 외부라이브러리 설치 해보기
$ pip install requests bs4
$ pip install fastapi uvicorn

```


## FastAPI 명령어

```sh
# FastAPI 실행 (main.py 실행) (기본 8000 포트)
# Swagger : http://127.0.0.1:8000/docs
# uvicorn main:app --reload

$ uvicorn main:app --reload --host 0.0.0.0 --port 7000

# main:app: 이 부분은 FastAPI 애플리케이션이 위치한 모듈과 애플리케이션 인스턴스를 지정.
# --reload: 코드 변경 시 서버가 자동으로 재시작되도록 함. 개발 시 유용.
# --host 0.0.0.0: 서버를 모든 네트워크 인터페이스에서 접근 가능하게 함. 로컬에서만 접근할 경우 --host 127.0.0.1을 사용.
# --port 7000: 서버가 리스닝할 포트 번호를 지정.

```