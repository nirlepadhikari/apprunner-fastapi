from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "suckers"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

#kick off build