from fastapi import FastAPI

app = FastAPI()

# request GET method url: "/"

# Path operation decorator
@app.get("/")
# root is the method name
async def root():
    return {"message": "welcome to my API!!"}

@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}
