import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from ast import literal_eval
from typing import List, Dict

class MovieRecommenderService:
    def __init__(self, data_path: str):
        self.df = self._load_data(data_path)
        self._prepare_data()
        self._build_similarity_matrix()

    def _load_data(self, path: str) -> pd.DataFrame:
        """Загрузка данных с обработкой ошибок"""
        try:
            df = pd.read_csv(path)
            required_columns = ['title', 'genres', 'vote_average']
            if not all(col in df.columns for col in required_columns):
                raise ValueError("Отсутствуют обязательные колонки в данных")
            return df
        except Exception as e:
            raise ValueError(f"Ошибка загрузки данных: {str(e)}")

    def _prepare_data(self):
        """Подготовка данных"""
        self.df['genres_list'] = self.df['genres'].apply(
            lambda x: [g['name'] for g in literal_eval(x)] if pd.notna(x) else []
        )
        self.df['combined_features'] = self.df['genres_list'].apply(lambda x: ' '.join(x))

    def _build_similarity_matrix(self):
        """Построение матрицы схожести"""
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['combined_features'])
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def recommend_by_movie(self, title: str, n: int = 5) -> List[Dict]:
        """Рекомендации по фильму"""
        try:
            idx = self.df[self.df['title'].str.lower() == title.lower()].index[0]
            sim_scores = list(enumerate(self.cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            movie_indices = [i[0] for i in sim_scores[1:n+1]]
            
            return [{
                "id": int(self.df.iloc[i]['id']),
                "title": str(self.df.iloc[i]['title']),
                "similarity_score": float(sim_scores[i][1]),
                "vote_average": float(self.df.iloc[i]['vote_average']),
                "genres": list(self.df.iloc[i]['genres_list'])
            } for i in movie_indices]
            
        except Exception as e:
            print(f"Ошибка в recommend_by_movie: {str(e)}")
            return []