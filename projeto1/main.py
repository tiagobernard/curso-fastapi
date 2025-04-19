from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router=router)

@app.get("/hello-world")
def hello_word():
    return {"Hello": "World"}