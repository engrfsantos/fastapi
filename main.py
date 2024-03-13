from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rate: Optional[int] = None
    
while True:
        
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', 
                                user='postgres', password='postgres', port='5441',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Banco de Dados Conectado corretamente')
        break
    except Exception as error:
        print('Erro na conexão do Banco de Dados')
        print('Erro Foi:' , error)
        time.sleep(2)


my_posts = [{"title":"primeiro título","content":"primeiro conteúdo","id":1},
            {"title":"segundo título","content":"segundo conteúdo","id":2},
            {"title":"terceiro título","content":"terceiro conteúdo","id":3}
            ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def read_root():
    return {"Hello": "Fast API"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM POSTS""")
    posts = cursor.fetchall()
    return {"Posts" : posts}

@app.get("/posts/lasted")
def get_lasted():
    print("Entrou na função Lasted")
    post = my_posts[len(my_posts)-1]
    print("Este é o post" , post)
    return {"Last Post" : post}

@app.get("/posts/{id}")
def read_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} Not Found")
    return {"Post": f"Este é o Post: {post}"}

@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def post_mensagem(post: Post):
    new_post = post.dict()
    new_post['id'] = randrange(0,1000000000)
    my_posts.append(new_post)
    return{"New Post" : post}

@app.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def post_delete(id: int):
    # deletando o post
    # encontra o índice na matriz requerido por ID
    # my_posts.pop(id)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"o id {id} não foi encontrado")
        
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    
@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    print(id, post)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} Not Found")
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"date": f"Postagem Atualizada: {post_dict}"}