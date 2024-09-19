from .db import db, environment, SCHEMA, add_prefix_for_prod

manga_genre = db.Table(
    'manga_genre',
    db.Column('manga_id', db.Integer, db.ForeignKey(add_prefix_for_prod('manga.id')), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey(add_prefix_for_prod('genre.id')), primary_key=True)
)

if environment == "production":
    manga_genre.schema = SCHEMA
