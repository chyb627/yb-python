## FastAPI
- Restful API를 구축하기 위한 파이썬 웹 프레임워크.

## URL
- URL 구성요소
    0. http://www.domain.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument
    1. Scheme : ex. http, https
    2. Domain Name : ex. www.domain.com
    3. Port : ex. 80, 443, 8000, 8080
    4. Path to the file : ex. /path/to/myfile.html
    5. Parameters : ex. ?key1=value1&key2=value2
    6. Anchor : ex. #SomewhereInTheDocument

## Parameters
1. Query Parameters
    - /func?key1=val1&key2=val2
2. Path Parameters
    - /func/val1
    - /func/val2?key1=val1
3. Cookie Parameters
4. Header Parameters
    - Header는 HTTP Header를 말함.
    - HTTP 요청과 응답시 함께 송신되는 정보.
    - 인코딩, 세션, 쿠키, IP, 브라우저 정보등.
    - 특수한 용도로 임의의 정보를 추가하여 활용할 수 있음.

## GET / POST / PUT / DELETE
- GET : 리소스 데이터의 수신, Read
- POST : 리소스 데이터의 생성, Create
- PUT : 리소스 데이터의 업데이트, Update
- DELETE : 리소스 데이터의 삭제, Delete or Remove

## OPTIONS / HEAD / PATCH / TRACE
- OPTIONS : 리소스 데이터의 허용, Request Methods
- HEAD : 리소스 데이터 GET 요청의 Header 정보 수신
- PATCH : 리소스 데이터의 업데이트
- TRACE : 리소스 데이터 접근까지의 경로 정보