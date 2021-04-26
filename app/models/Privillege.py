#--coding:utf-8--

from app.models import db


class Privillege(db.Model):
    __tablename__='privillege'
    pid=db.Column(db.Integer,primary_key=True,unique=True)
    dept=db.Column(db.String(100))
    permissions=db.Column(db.Integer)



	
