from vadhyam import db,app

from flask_table import Table, Col, LinkCol






class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    contact = db.Column(db.String(80))
    usertype = db.Column(db.String(80))





