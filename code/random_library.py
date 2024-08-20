import random

for i in range(0, 5):
    print(random.randint(1, 30))
    print(random.randint(10000000, 99999999))

# 과일 바구니에서 랜덤으로 뽑기
basket = ["사과", "복숭아", "레몬", "블루베리"]
print(random.choice(basket))