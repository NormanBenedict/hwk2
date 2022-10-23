from app import db

# Define the DB schema
class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    origin = db.Column(db.String(16), unique=False, nullable=False)
    mpg = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.origin}, {self.mpg}"
