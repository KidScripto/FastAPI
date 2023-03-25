from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

## Resume 39.24
## https://www.youtube.com/watch?v=0sOvCWFmrtA&t=730s