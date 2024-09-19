from app.models import db, Genre, environment, SCHEMA
from sqlalchemy import text

def seed_genres():
    genres = [
        Genre(name="Adventure"),
        Genre(name="Fantasy"),
        Genre(name="Action"),
        Genre(name="Drama"),
        Genre(name="Superhero"),
        Genre(name="Supernatural"),
        Genre(name="Martial Arts"),
        Genre(name="Thriller"),
        Genre(name="Horror"),
        Genre(name="Mystery"),
        Genre(name="Comedy"),
        Genre(name="Romance"),
        Genre(name="Sci-Fi"),
        Genre(name="Cooking"),
        Genre(name="Sports"),
        Genre(name="Historical"),
    ]

    for genre in genres:
        db.session.add(genre)

    db.session.commit()

def undo_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.genre RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM genre"))

    db.session.commit()
