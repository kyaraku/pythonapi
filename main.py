from typing import Optional
from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"ttle": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"ttle": "favorite foods", "content": "I like pineapple pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}
    # return {"data": "This is your posts"}
    
 
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data" : post_dict}
    # print(post)
    # print(post.dict())
    # return {"data" : post}

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

@app.get("/posts/{id}")   
def get_post(id: int, response: Response):
    # print(type(id))
    post = find_post(id)
    if not post:
        response.status_code = 404
    return {"post_detail" : post}
    # return {"post_detail": f"Here is post {id}"}
    
