#--coding:utf-8--
from app.models import db
class LateBack(db.Model):
    __tablename__ = 'lateback'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    time = db.Column(db.DateTime(), nullable=False)
    recorder = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    def __init__(self, **kwargs):
        super(LateBack, self).__init__(**kwargs)
    

def add(**kwargs):
    try:
        record = LateBack(**kwargs)
        db.session.add(record)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def query():
    try:
        return LateBack.query.all()
    except Exception as e:
        return None

def modify(id, modify_info):
    record = LateBack.query.filter_by(id=id).first()
    if record is None:
        return False, "No such record."
    else:
        try:
            for key in modify_info:
                if key == 'user_id':
                    record.user_id = modify_info[key]
                elif key == 'time':
                    record.time = modify_info[key]
                elif key == 'recorder':
                    record.recorder = modify_info[key]
            db.session.commit()
            return True, "Modify success"
        except Exception as e:
            print(e)
            db.session.rollback()
            return False, "Exception appear."

def delete(id):
    record = LateBack.query.filter_by(id=id).first()
    if record is None:
        return False, "No such record."
    else:
        db.session.delete(record)
        db.session.commit()
        return True, "Delete success."

