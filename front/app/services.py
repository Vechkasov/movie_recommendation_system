import requests
from typing import List, Dict, Optional

class MovieRecommenderService:
    def __init__(self, api_url: str = "http://localhost:8000"):
        self.api_url = api_url

    def get_recommendations(self, title: str) -> List[Dict]:
        """Получить рекомендации по фильму"""
        try:
            response = requests.post(
                f"{self.api_url}/recommendations",
                json={"movie_title": title, "n_recommendations": 5}
            )
            return response.json().get('recommendations', [])
        except:
            return []