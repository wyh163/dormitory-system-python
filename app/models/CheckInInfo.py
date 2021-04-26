#--coding:utf-8--
from app.models import db
class CheckIn(db.Model):
    __tablename__ = 'checkin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    checkin_time = db.Column(db.DateTime())
    checkout_time = db.Column(db.DateTime())
    checkin_recorder = db.Column(db.String(20), nullable=False)
    checkout_recorder = db.Column(db.String(20), nullable=False)
    checkin_things = db.Column(db.String(100))
    def __init__(self, **kwargs):
        super(CheckIn, self).__init__(**kwargs)


def add(**kwargs):
    try:
        records = CheckIn(**kwargs)
        db.session.add(records)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def query(id):
    try:
        records = CheckIn.query.filter_by(id=id).first()
        return records
    except Exception as e:
        print(e)
        return None

def query_all():
    return CheckIn.query.all()

def modify(id, modify_info):
    try:
        records = CheckIn.query.filter_by(id=id).first()
        # return records
        for key in modify_info:
            if (key == 'user_id'):
                records.user_id = modify_info[key]
            elif (key == 'checkin_time'):
                records.checkin_time = modify_info[key]
            elif (key == 'checkout_time'):
                records.checkout_time = modify_info[key]
            elif (key == 'checkin_things'):
                records.checkin_things = modify_info[key]
            elif (key == 'checkin_recorder'):
                records.checkin_recorder = modify_info[key]
            elif (key == 'checkout_recorder'):
                records.checkout_recorder = modify_info[key]
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False

def delete(id):
    try:
        records = CheckIn.query.filter_by(id=id).first()
        # return records
        db.session.delete(records)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False