from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int = Field(..., ge=1900)


books: List[Book] = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add CRUD routes for books here
