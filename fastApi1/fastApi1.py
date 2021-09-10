from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

app = FastAPI()

# pip install uvicorn
# uvicorn fastApi1:app --reload //运行 或者直接运行main方法
# http://127.0.0.1:8000/docs    //交互文档
# http://127.0.0.1:8000/redoc  //API文档


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World2232"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == '__main__':
    uvicorn.run("fastApi1:app",host="0.0.0.0",port=8000,reload=True,workers = 2);
    print("程序启动完成");