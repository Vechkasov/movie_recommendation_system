from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class Genre(BaseModel):
    id: int
    name: str

class Keyword(BaseModel):
    id: int
    name: str

class ProductionCompany(BaseModel):
    id: int
    name: str

class ProductionCountry(BaseModel):
    iso_3166_1: str
    name: str

class SpokenLanguage(BaseModel):
    iso_639_1: str
    name: str

class Movie(BaseModel):
    id: int
    title: str
    original_title: str
    overview: Optional[str] = None
    tagline: Optional[str] = None
    budget: Optional[int] = None
    revenue: Optional[int] = None
    popularity: float
    vote_average: float
    vote_count: int
    runtime: Optional[int] = None
    release_date: Optional[str] = None
    genres: List[Genre]
    keywords: List[Keyword]
    production_companies: List[ProductionCompany]
    production_countries: List[ProductionCountry]
    spoken_languages: List[SpokenLanguage]
    status: Optional[str] = None
    homepage: Optional[str] = None
    original_language: Optional[str] = None

    class Config:
        from_attributes = True  #