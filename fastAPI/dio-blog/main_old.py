from datetime import datetime, UTC
from typing import Annotated
from fastapi import Cookie, FastAPI, Header, Response

# acessar o path
# C:\Users\pedro\AppData\Local\pypoetry\Cache\virtualenvs\dio-blog-0s_JxyXF-py3.14\Scripts\activate.bat
# pra rodar o projeto
# uvicorn main:app --reload
# poetry run python -m uvicorn main:app --reload
# poetry run uvicorn main:app --reload


app = FastAPI()

fake_infos = [
    {"message": "teste do aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "então esse e o aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "teste do aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "então esse e o aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "teste do aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "então esse e o aaaaa", "date": datetime.now(UTC), "published": True},
]


@app.get("/")
def read_root():
    return {"message": "hello world", "lets": "see"}


# parametro na URL devem ser passados da seguinte forma:
# infos?skip=1&limit=1
@app.get("/infos")
def read_infos(skip: int = 0, limit: int = 0):
    return fake_infos[skip : skip + limit]


# parametro do tipo booleanos devem ser passados da seguinte forma:
# infos?on
# infos?off
# infos?True || infos?true
# infos?1
# infos?0
# infos?yes
# infos?no
@app.get("/infos")
def read_infos_bool(published: bool):
    return [post for post in fake_infos if post["published"] is published]


@app.get("/posts/{assunto}")
def read_posts(assunto):
    return {
        "posts": [
            {"message": f"teste do {assunto}", "date": datetime.now(UTC)},
            {"message": f"então esse e o {assunto}", "date": datetime.now(UTC)},
        ]
    }


@app.get("/posts/{assunto}")
def read_posts_tipagem(
    assunto: str,
):  # se não for passado o tipo corretamente gera um erro
    return {
        "posts": [
            {"message": f"teste do {assunto} em str", "date": datetime.now(UTC)},
            {"message": f"então esse e o {assunto} em str", "date": datetime.now(UTC)},
        ]
    }


@app.get("/cookie/")
async def read_cookie(
    response: Response, ads_id: Annotated[str | None, Cookie()] = None
):
    response.set_cookie(key="user", value="valor da key")
    print(f"cookie {ads_id}")
    return {"ads_id": ads_id}


@app.get("/header/")
async def read_header(user_agent: Annotated[str | None, Header()] = None):
    print(f"Header {user_agent}")
    return {"Header": user_agent}
