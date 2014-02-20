from app import db

class Q_MOD(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.Text, index = True, unique = True)
    answer = db.Column(db.Text, index = True)
