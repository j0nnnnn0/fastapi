from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating : Optional[int] = None

# request GET method url: "/"
# Path operation decorator
@app.get("/")
# root is the method name
async def root():
    return {"message": "welcome to my API!!"}

@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}

# posting 
# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']}, content {payload['content']}"}


# Create a post 
@app.post("/posts")
def create_posts(post : Post):
    print(post)
    print (post.dict()) # convert to dictionary
    # return {"new_post": f"title: {new_post.title},content: {new_post.content},published: {new_post.published},rating: {new_post.rating}"}
    return {"data": post}

