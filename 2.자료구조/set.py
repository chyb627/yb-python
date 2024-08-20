empry_set = set() # empry_set = {}로 선언하면 딕셔너리가 된다.
my_set = {1, 2, 3, 3} # 중복된 값은 버려지고 유니크한 값만 저장됨.
print(my_set)

# 과일 바구니
fruits = {"apple", "banana", "blueberry"}
fruits.add("orange")
print(fruits) # 순서가 없음 -> 대괄호를 통한 인덱스 접근이 불가능
fruits.remove("banana")
print(fruits)

fruits1 = {"apple", "strawberry", "peach"}
fruits2 = {"banana", "strawberry", "orange"}
# 합집합
union = fruits1.union(fruits2) # union = fruits1 | fruits2 도 동일한 결과값이 나옴
print(union) # {'strawberry', 'apple', 'orange', 'peach', 'banana'}
# 교집합
intersection = fruits1.intersection(fruits2)
print(intersection) # {'strawberry'}
# 차집합
diff1 = fruits1.difference(fruits2)
diff2 = fruits2.difference(fruits1)
print(diff1) # {'apple', 'peach'}
print(diff2) # {'orange', 'banana'}