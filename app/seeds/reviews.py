from app.models import db, Review, User, Manga, environment, SCHEMA
from sqlalchemy import text
from datetime import datetime

def seed_reviews():
    user1 = User.query.get(1)
    user2 = User.query.get(2)
    user3 = User.query.get(3)

    mangas = Manga.query.all()

    reviews = []

    for manga in mangas:
        reviews.extend([
            Review(rating=5, content=f"{manga.title} is an outstanding manga with great plot and character development!", manga_id=manga.id, user_id=user1.id, timestamp=datetime.utcnow()),
            Review(rating=4, content=f"I really enjoyed reading {manga.title}, but some arcs felt a bit dragged.", manga_id=manga.id, user_id=user2.id, timestamp=datetime.utcnow())
        ])

    for review in reviews:
        db.session.add(review)

    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.review RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM review"))

    db.session.commit()
