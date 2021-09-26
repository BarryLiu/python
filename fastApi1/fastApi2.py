from fastapi import FastAPI
import uvicorn

app  = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World2232"}


if __name__ == '__main__':
    uvicorn.run("fastApi2:app",host="0.0.0.0",port=8000,reload=True,workers = 2);
    print("程序启动完成");