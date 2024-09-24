from flask import Blueprint, jsonify, request
from app.models import Manga, db
from flask_login import current_user, login_required
from datetime import datetime

manga_routes = Blueprint('manga', __name__)

@manga_routes.route('/')
def manga_index():
    mangas = Manga.query.all()

    return [manga.to_dict() for manga in mangas]
