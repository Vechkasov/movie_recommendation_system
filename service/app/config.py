import os
from pathlib import Path

class Settings:
    DATA_PATH: str = str(Path(__file__).parent.parent / "data" / "movies.csv")
    API_TITLE: str = "Movie Recommendation API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API для получения рекомендаций фильмов на основе ML"

settings = Settings()