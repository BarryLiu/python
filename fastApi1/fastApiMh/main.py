from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn

from mh import  app_mh

app  = FastAPI()

app.include_router(app_mh, prefix='/mh', tags=['测试接口'])

# mount表示将某个目录下一个完全独立的应用挂载过来，这个不会在API交互文档中显示
app.mount(path='/static', app=StaticFiles(directory='./mh/static'), name='static')  # .mount()不要在分路由APIRouter().mount()调用，模板会报错


@app.get("/")
def read_root():
    return {"Helloworld": "this just is a test !"}


if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True,workers = 2);
    print("程序启动完成");