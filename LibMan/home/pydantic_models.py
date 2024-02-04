from pydantic import BaseModel

class BookCreateUpdateModel(BaseModel):
    title: str
    author: str
    publication_year: int

class ReviewCreateModel(BaseModel):
    text: str
    rating: int