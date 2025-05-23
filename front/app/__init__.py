from flask import Flask
from .routes import bp as recommendations_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(recommendations_bp)
    
    return app