from app import db

# THIS IS OUR DATABASE MODEL (FOR OUR POSTS)
class my_posts(db.Model):
    # __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(12))
    description = db.Column(db.String(200))
    photo = db.Column(db.LargeBinary)

    # def __init__(self, date, description, photo):
    #     self.date = date
    #     self.description = description
    #     self.photo = photo