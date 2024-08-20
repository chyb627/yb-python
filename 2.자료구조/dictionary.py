person = {"name": "홍길동", "age": "30", "city": "서울"}
name = person["name"] # 홍길동
print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.")

country = person.get("country", "알수 없음") # 값이 없을 경우가 있으므로  person["country"] 보다는 get을 사용하는 것이 안전한 방법이다.
print(f"국적은 {country}입니다.")

person["age"] = 35 # {'name': '홍길동', 'age': 35, 'city': '서울'}
person["country"] = "대한민국" # {'name': '홍길동', 'age': 35, 'city': '서울', 'country': '대한민국'}
country = person.get("country", "알수 없음")
print(f"국적은 {country}입니다.")

person_detail = {"married": True, "company": "apple"}
person.update(person_detail) # {'name': '홍길동', 'age': 35, 'city': '서울', 'country': '대한민국', 'married': True, 'company': 'apple'}
print(person)
print(person.keys()) # dict_keys(['name', 'age', 'city', 'country', 'married', 'company'])

del person["married"]
print(person.keys()) # dict_keys(['name', 'age', 'city', 'country', 'company'])