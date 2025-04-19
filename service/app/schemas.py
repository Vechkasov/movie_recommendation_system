from typing import List, Optional
from pydantic import BaseModel

class MovieRecommendation(BaseModel):
    id: int
    title: str
    similarity_score: float
    vote_average: float
    genres: List[str]

class RecommendationRequest(BaseModel):
    movie_title: Optional[str] = None
    features: Optional[str] = None
    n_recommendations: int = 10

class PopularMoviesRequest(BaseModel):
    n_recommendations: int = 10
    min_votes: int = 100