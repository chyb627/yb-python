from typing import Union
from fastapi import Cookie, FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    # price: float
    # tax: float | None = None

fake_items_db = [{"name": "Cha", "description": "One"}, {"name": "You", "description": "Two"}, {"name": "Bin",  "description": "Three"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# http://127.0.0.1:8000/items/?skip=0&limit=10
# 몇번째부터 몇개를 가져오는지에 관한 쿼리파람
# 함수의 파라미터에 수신할 파라미터의 키를 지정해준다.
# 패스 파라미터와의 차이점은 데코레이터 파라미터에서 별도의 값을 지정하지 않는다.
# 즉, 데코레이터 파라미터에서 패스파라미터를 지정하지 않았으나, 함수에서 파라미터를 수신한다고 정의하면 (skip, limit) 쿼리파라미터를 수신한다는 뜻
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return fake_items_db[item_id - 1]

@app.post("/items/")
async def create_item(item: Item):
    fake_items_db.append(item)
    print(fake_items_db)
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    fake_items_db[item_id - 1] = item
    return fake_items_db[item_id - 1]

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    fake_items_db.remove(fake_items_db[item_id - 1])
    return {item_id: item_id}

# 쿠키에 개인정보가 될만한 내용은 절대로 저장하면 안된다.
@app.get("/items/cookie/")
def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}

@app.get("/items/header/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
