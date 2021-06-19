"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    __tablename__ = 'cupcakes'
    
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    
    flavor = db.Column(db.Text,
                        nullable=False)
    
    size = db.Column(db.Text,
                        nullable=False)
    
    rating = db.Column(db.Float,
                        nullable=False)
    
    image = db.Column(db.Text,
                        default="https://tinyurl.com/demo-cupcake")
    
    def serialize(self):
        """Returns a dict representation of Cupcake which we can turn into JSON"""
        c = self
        return {
            'id': c.id,
            'flavor': c.flavor,
            'size': c.size,
            'rating': c.rating,
            'image': c.image
        }

    def __repr__(self):
        c = self
        return f"<Cupcake {c.id} flavor={c.flavor} size={c.size} rating={c.rating} image={c.image}>"