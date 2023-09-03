import re
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating : Optional[int] = None

# creating a dictionary to keep posts in memory
my_posts = [{"title": "title1", "content": "content1", "published": True, "rating": 5, "id": 1},
            {"title": "favorite food", "content": "pizza", "published": True, "rating": 4, "id": 2}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
    return None

# request GET method url: "/"
# Path operation decorator
@app.get("/")
# root is the method name
async def root():
    return {"message": "welcome to my API!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# posting 
# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']}, content {payload['content']}"}

# Create a post 
@app.post("/posts")
def create_posts(post : Post):
    # print(post)
    # print (post.dict()) # convert to dictionary
    # return {"new_post": f"title: {new_post.title},content: {new_post.content},published: {new_post.published},rating: {new_post.rating}"}
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100000000)
    my_posts.append(post_dict) # append to my_posts
    return {"data": post_dict}

# Get a single post by ID
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    print(post)
    return {"post_detail": post}