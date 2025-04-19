### Примеры запросов:
1. Получить рекомендации по фильму:
    ```bash
    curl -X POST "http://localhost:8000/recommendations" \
    -H "Content-Type: application/json" \
    -d '{"movie_title": "Avatar", "n_recommendations": 5}'
    ```
2. Получить рекомендации по признакам:
    ```bash
    curl -X POST "http://localhost:8000/recommendations" \
    -H "Content-Type: application/json" \
    -d '{"features": "science fiction space adventure", "n_recommendations": 5}'
    ```
3. Получить популярные фильмы:
    ```bash
    curl -X POST "http://localhost:8000/popular" \
    -H "Content-Type: application/json" \
    -d '{"n_recommendations": 5, "min_votes": 1000}'
    ```
4. Поиск фильмов:
    ```bash
    curl "http://localhost:8000/search/?query=pirates&limit=3"
    ```

### Примеры ответов
Запрос для анимационных фильмов
```json
{
  "recommendations": [
    {
      "id": 16690,
      "title": "Return to Never Land",
      "similarity_score": 0.29428261041472836,
      "vote_average": 6.1,
      "genres": [
        "Adventure",
        "Fantasy",
        "Animation",
        "Family"
      ]
    },
    {
      "id": 7450,
      "title": "Titan A.E.",
      "similarity_score": 0.2729509979945124,
      "vote_average": 6.3,
      "genres": [
        "Animation",
        "Action",
        "Science Fiction",
        "Family",
        "Adventure"
      ]
    },
    {
      "id": 239897,
      "title": "Dwegons",
      "similarity_score": 0.26262230959624666,
      "vote_average": 0.5,
      "genres": [
        "Animation"
      ]
    },
    {
      "id": 9023,
      "title": "Spirit: Stallion of the Cimarron",
      "similarity_score": 0.2560592551340744,
      "vote_average": 7.4,
      "genres": [
        "Western",
        "Animation",
        "Adventure",
        "Comedy",
        "Family"
      ]
    },
    {
      "id": 228326,
      "title": "The Book of Life",
      "similarity_score": 0.2426654066699001,
      "vote_average": 7.3,
      "genres": [
        "Romance",
        "Animation",
        "Adventure",
        "Comedy",
        "Family",
        "Fantasy"
      ]
    }
  ],
  "metadata": {
    "count": 5,
    "average_similarity": 0.2657161159618924,
    "average_rating": 5.52
  }
}
```

### API Endpoints
POST `/recommendations` - Получить рекомендации

GET `/search` - Поиск фильмов по названию

GET `/genres` - Список всех жанров