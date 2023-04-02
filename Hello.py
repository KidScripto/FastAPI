from fastapi import FastAPI
from fastapi.params import Body 

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is a post"}
## start server with uvicorn Hello:app --reload

@app.post("/createposts")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}