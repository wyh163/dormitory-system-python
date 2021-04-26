#--coding:utf-8--
from app.models import db
class LeaveRecord(db.Model):
    __tablename__ = "leave_record"
    record_id = db.Column(db.INTEGER,primary_key=True, autoincrement=True)    
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    time = db.Column(db.DateTime(), nullable=False)
    _class = db.Column(db.Text)
    recorder = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self,**kwargs):
        super(LeaveRecord,self).__init__(**kwargs)

def query():
    records = LeaveRecord.query.all()
    return records

def add(**kwargs):
    try:
        leaveRecord=LeaveRecord(**kwargs)
        db.session.add(leaveRecord)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def modify(record_id, modify_info):
    try:
        leaveRecord=LeaveRecord.query.filter_by(record_id=record_id).first()
        for key in modify_info:
            if key == 'user_id':
                leaveRecord.user_id = modify_info[key]
            elif key == 'time':
                leaveRecord.time = modify_info[key]
            elif key == '_class':
                leaveRecord._class = modify_info[key]
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
    
def delete(record_id):
    try:
        leaveRecord=LeaveRecord.query.filter_by(record_id=record_id).first()
        db.session.delete(leaveRecord)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False