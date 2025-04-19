from flask import Blueprint, request, render_template
import requests

bp = Blueprint('main', __name__)
API_URL = "http://localhost:8000"

@bp.route('/', methods=['GET', 'POST'])
def index():
    error = None
    recommendations = []
    search_title = ""
    
    if request.method == 'POST':
        search_title = request.form.get('title', '')
        try:
            response = requests.post(
                f"{API_URL}/recommendations",
                json={"movie_title": search_title, "n_recommendations": 5},
                timeout=10
            )
            response.raise_for_status()
            recommendations = response.json()
        except requests.exceptions.RequestException as e:
            error = f"Ошибка сервера: {str(e)}"
    
    return render_template(
        'index.html',
        recommendations=recommendations,
        search_title=search_title,
        error=error
    )