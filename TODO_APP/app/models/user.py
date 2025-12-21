from app import db
class User(db.Model):
    id=db.Column(db.Integer, primary_key= True)
    username=db.Column(db.Integer, unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    
