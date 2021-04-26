#--coding:utf-8--

from app.models import db
from datetime import datetime

class Check(db.Model):
    __tablename__='insert_check'
    check_id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    url=db.Column(db.String(256),unique=True,nullable=False)

    def __repr__(self):
        return  '<Check: %r %r>' % (self.check_id,self.url)

    def __init__(self,**kwargs):
        super(Check,self).__init__(**kwargs)

def insert(**kwargs):
    try:
        check=Check(**kwargs)
        db.session.add(check)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def delete(cid):
    try:
        check = Check.query.filter_by(check_id=cid).first()
        db.session.delete(check)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def query():
    res=Check.query.order_by('check_id').all()
    return res

def isExists(insert_url):
    res=Check.query.filter(Check.url==insert_url).first()
    if res:
        return True
    else:
        return False
