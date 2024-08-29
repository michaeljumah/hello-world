from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel 
from typing import Optional


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None
    
        


@app.get("/")
async def root():
    return {"message": "Jambo Kenya"}


@app.get("/getuser")
async def get_user():
    user = input(str("Enter your name: "))
    return {"message ": f"hello {user}"}


@app.post("/creatposts")
async def create_post(new_post: Post):
    print(new_post.rating)
    return {"data": "new_post"}