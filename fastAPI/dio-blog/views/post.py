from pydantic import AwareDatetime, BaseModel, NaiveDatetime
from datetime import UTC, datetime


# class PostOut(BaseModel):
#     id: int
#     title: str
#     content: str
#     published_at: AwareDatetime | NaiveDatetime | None


class PostOut(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    publised: bool
