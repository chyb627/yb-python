my_list = [10, 20, 30]
my_list.append(40)
my_list.append(50)
my_list.append(60)
print(my_list)
print(len(my_list))
print(my_list[4])

sliced = my_list[3:]
print("Sliced: ", sliced)

fruits = ["banana", "apple", "blueberry", "cherry"]
# 바나나가 포함되어 있나요?
is_banana_included = "banana" in fruits
is_orange_included = "orange" in fruits
print("Is banana included? ", is_banana_included)
print("Is orange included? ", is_orange_included)
# 체리는 어디에 있나요?
index_cherry = fruits.index("cherry")
print("Cherry is", index_cherry)

# 리스트의 정렬
numbers = [4, 2, 1, 3, 8, 6, 7, 5]
print("Unsorted::", numbers)
numbers.sort()
print("Sorted::", numbers)
numbers.sort(reverse=True)
print("Sorted Reverse::", numbers)

# 리스트의 요소 추가 및 제거
my_list2 = []
my_list2.append(10) # [10]
my_list2.append(11) # [10, 11]
my_list2.append(12) # [10, 11, 12]
my_list2.extend([13, 14, 15]) # [10, 11, 12, 13, 14, 15] # 하나의 리스트가 됨
my_list2.append([16, 17, 18]) # [10, 11, 12, 13, 14, 15, [16, 17, 18]] # 복합리스트가 됨
print(my_list2)

# 리스트 연산 (+, *)
my_list3 = [10, 11, 12, 13, 14, 15]
new_list = my_list3 + [0, 1, 2]
print(new_list) # [10, 11, 12, 13, 14, 15, 0, 1, 2]
multi_list = [0, 1, 3] * 3
print(multi_list) # [0, 1, 3, 0, 1, 3, 0, 1, 3]
del my_list3[0]
print(my_list3) # [11, 12, 13, 14, 15]

max_value = max(my_list3)
min_value = min(my_list3)
print(f"최대값은 {max_value}, 최소값은 {min_value} 입니다.")