from datetime import UTC, datetime
from typing import Annotated
from fastapi import APIRouter, Cookie, Depends, Header, Response, status

from schemas.post import PostIn, PostUpdateIn

# from security import login_required
# from services.post import PostService
from views.post import PostOut

# router = APIRouter(prefix="/posts", dependencies=[Depends(login_required)])
router = APIRouter(prefix="/posts")

# service = PostService()


# @router.get("/", response_model=list[PostOut])
# async def read_posts(published: bool, limit: int, skip: int = 0):
#     return await service.read_all(published=published, limit=limit, skip=skip)


# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
# async def create_post(post: PostIn):
#     return {**post.model_dump(), "id": await service.create(post)}


# @router.get("/{id}", response_model=PostOut)
# async def read_post(id: int):
#     return await service.read(id)


# @router.patch("/{id}", response_model=PostOut)
# async def update_post(id: int, post: PostUpdateIn):
#     return await service.update(id=id, post=post)


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
# async def delete_post(id: int):
#     await service.delete(id)


fake_infos = [
    {"message": "teste do aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "então esse e o aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "teste do aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "então esse e o aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "teste do aaaaa", "date": datetime.now(UTC), "published": True},
    {"message": "então esse e o aaaaa", "date": datetime.now(UTC), "published": True},
]


@router.get("/")
def read_root():
    return {"message": "hello world", "lets": "see"}


# parametro na URL devem ser passados da seguinte forma:
# infos?skip=1&limit=1
@router.get("/infos")
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
@router.get("/infos")
def read_infos_bool(published: bool):
    return [post for post in fake_infos if post["published"] is published]


@router.get("/posts/{assunto}")
def read_posts(assunto):
    return {
        "posts": [
            {"message": f"teste do {assunto}", "date": datetime.now(UTC)},
            {"message": f"então esse e o {assunto}", "date": datetime.now(UTC)},
        ]
    }


@router.get("/posts/{assunto}")
def read_posts_tipagem(
    assunto: str,
):  # se não for passado o tipo corretamente gera um erro
    return {
        "posts": [
            {"message": f"teste do {assunto} em str", "date": datetime.now(UTC)},
            {"message": f"então esse e o {assunto} em str", "date": datetime.now(UTC)},
        ]
    }


@router.get("/cookie/")
async def read_cookie(
    response: Response, ads_id: Annotated[str | None, Cookie()] = None
):
    response.set_cookie(key="user", value="valor da key")
    print(f"cookie {ads_id}")
    return {"ads_id": ads_id}


@router.get("/header/")
async def read_header(user_agent: Annotated[str | None, Header()] = None):
    print(f"Header {user_agent}")
    return {"Header": user_agent}
