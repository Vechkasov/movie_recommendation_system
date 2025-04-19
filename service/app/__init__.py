from .main import app
from .models import Movie, Genre, Keyword, ProductionCompany, ProductionCountry, SpokenLanguage
from .schemas import MovieRecommendation, RecommendationRequest, PopularMoviesRequest
from .services import MovieRecommenderService
from .config import settings

__all__ = [
    'app',
    'Movie',
    'Genre',
    'Keyword',
    'ProductionCompany',
    'ProductionCountry',
    'SpokenLanguage',
    'MovieRecommendation',
    'RecommendationRequest',
    'PopularMoviesRequest',
    'MovieRecommenderService',
    'settings'
]