from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rate: Optional[int] = None

my_posts = [{"title":"primeiro título","content":"primeiro conteúdo","id":1},
            {"title":"segundo título","content":"segundo conteúdo","id":2},
            {"title":"terceiro título","content":"terceiro conteúdo","id":3}
            ]


@app.get("/")
async def read_root():
    return {"Hello": "Fast API"}

@app.get("/posts")
async def read_posts():
    return {"Posts" : my_posts}


@app.get("/posts/lasted")
async def get_lasted():
    print("Entrou na função Lasted")
    post = my_posts[len(my_posts)-1]
    print("Este é o post" , post)
    return {"Last Post" : post}

@app.get("/posts/{id}")
async def read_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} Not Found")
    return {"Post": f"Este é o Post: {post}"}

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.post("/createpost", status_code=status.HTTP_201_CREATED)
async def post_mensagem(post: Post):
    new_post = post.dict()
    new_post['id'] = randrange(0,1000000000)
    my_posts.append(new_post)
    return{"New Post" : post}
