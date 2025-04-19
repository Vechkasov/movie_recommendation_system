from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from ast import literal_eval
import os

app = FastAPI()

# Загрузка данных
DATA_PATH = 'data/movies.csv'

try:
    df = pd.read_csv(DATA_PATH)
    df['genres_list'] = df['genres'].apply(lambda x: [g['name'] for g in literal_eval(x)] if pd.notna(x) else [])
    df['combined_features'] = df['genres_list'].apply(lambda x: ' '.join(x))
    
    # Построение модели
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
except Exception as e:
    raise RuntimeError(f"Ошибка инициализации: {str(e)}")

class RecommendationRequest(BaseModel):
    movie_title: Optional[str] = None
    features: Optional[str] = None
    n_recommendations: int = 5

class MovieRecommendation(BaseModel):
    id: int
    title: str
    similarity_score: float
    vote_average: float
    genres: List[str]

@app.post("/recommendations", response_model=List[MovieRecommendation])
def get_recommendations(request: RecommendationRequest):
    try:
        if request.movie_title:
            # Поиск с учетом регистра
            matches = df[df['title'].str.lower() == request.movie_title.lower()]
            if matches.empty:
                raise HTTPException(status_code=404, detail="Фильм не найден")
            
            idx = matches.index[0]
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            movie_indices = [i[0] for i in sim_scores[1:request.n_recommendations+1]]
            
            return [{
                "id": int(df.iloc[i]['id']),
                "title": str(df.iloc[i]['title']),
                "similarity_score": float(sim_scores[i][1]),
                "vote_average": float(df.iloc[i]['vote_average']),
                "genres": list(df.iloc[i]['genres_list'])
            } for i in movie_indices]
            
        elif request.features:
            feature_vector = tfidf.transform([request.features])
            sim_scores = linear_kernel(feature_vector, tfidf_matrix).flatten()
            movie_indices = sim_scores.argsort()[::-1][:request.n_recommendations]
            
            return [{
                "id": int(df.iloc[i]['id']),
                "title": str(df.iloc[i]['title']),
                "similarity_score": float(sim_scores[i]),
                "vote_average": float(df.iloc[i]['vote_average']),
                "genres": list(df.iloc[i]['genres_list'])
            } for i in movie_indices]
            
        raise HTTPException(status_code=400, detail="Укажите movie_title или features")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/search")
def search_movies(query: str, limit: int = 5):
    try:
        matches = df[df['title'].str.lower().str.contains(query.lower())]
        return {
            "results": matches[['title', 'vote_average']].head(limit).to_dict('records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))