from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Bags(db.Model):
    __tablename__="bags"

    if environment == "production":
       __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.string(100), nullable=False)
    price = db.Column(db.string(100), nullable=False)
    images = db.column(db.String(255), nullable=True)
    date_listed = db.column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default="Available")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'images': self.images,
            'date_listed': self.date_listed.isoformat(),
            'status': self.status
        }
