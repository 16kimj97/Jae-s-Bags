from flask import Blueprint, jsonify, request
from app.models import Manga, db
from flask_login import current_user, login_required
from datetime import datetime

manga_routes = Blueprint('manga', __name__)

@manga_routes.route('/')
def manga_index():
    mangas = Manga.query.all()

    return [manga.to_dict() for manga in mangas]

@manga_routes.route('/<int:manga_id>', methods=['DELETE'])
@login_required
def delete_manga(manga_id):
    manga = Manga.query.get(manga_id)

    if not manga:
        return jsonify({"error": "Manga not found"}), 404

    db.session.delete(manga)
    db.session.commit()

    return jsonify({"message": "Manga deleted successfully"}), 200
