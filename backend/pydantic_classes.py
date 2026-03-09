from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

class Genre(Enum):
    Cookbooks = "Cookbooks"
    Philosophy = "Philosophy"
    Adventure = "Adventure"
    Thriller = "Thriller"
    Horror = "Horror"
    History = "History"
    Poetry = "Poetry"
    Fantasy = "Fantasy"
    Romance = "Romance"
    Technology = "Technology"

############################################
# Classes are defined here
############################################
class AuthorCreate(BaseModel):
    birth: date
    name: str
    books: List[int]  # N:M Relationship


class LibraryCreate(BaseModel):
    address: str
    web_page: str
    telephone: str
    name: str
    books: List[int]  # N:M Relationship


class BookCreate(BaseModel):
    pages: int
    release: date
    stock: int
    price: float
    genre: Genre
    title: str
    library: List[int]  # N:M Relationship
    authors: List[int]  # N:M Relationship

    @field_validator('pages')
    @classmethod
    def validate_pages_1(cls, v):
        """OCL Constraint: constraint_Book_0_1"""
        if not (v > 10):
            raise ValueError('pages must be > 10')
        return v

