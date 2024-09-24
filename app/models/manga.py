from .db import db, environment, SCHEMA, add_prefix_for_prod

class Manga(db.Model):
    __tablename__ = "manga"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    cover_image = db.Column(db.String(255), nullable=True)
    reviews = db.relationship('Review', backref='manga', lazy=True)

    genres = db.relationship('Genre', secondary=manga_genre, backref=db.backref('manga', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'cover_image': self.cover_image,
            'genres': [genre.to_dict() for genre in self.genres],  
            'reviews': self.reviews
        }
