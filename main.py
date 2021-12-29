from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"ttle": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"ttle": "favorite foods", "content": "I like pineapple pizza", "id": 2}]

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}
    # return {"data": "This is your posts"}

@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data" : post}

# Other ways for creating a post    
# def create_posts(new_post: Post):
#     print(new_post.rating)
#     # print(new_post.title)
#     return {"data" : "new post"}

# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"message": f"title: {payload['title']} content: {payload['content']}"}
    # return {"message": "successfuly created a post"}
    # title str, content str, category, Bool publi

