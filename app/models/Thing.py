from app.models import db

class InOutThing(db.Model):
    __tablename__ = "in_out_thing"
    record_id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)    
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    number = db.Column(db.Integer)
    
    def __init__(self,**kwargs):
        super(InOutThing,self).__init__(**kwargs)
    

def query():
    return InOutThing.query.all()

def add(**kwargs):
    try:
        inOutThing=InOutThing(**kwargs)
        db.session.add(inOutThing)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def modify(record_id, modify_info):
    try:
        inOutThing=InOutThing.query.filter_by(record_id=record_id).first()
        # inOutThing.
        for key in modify_info:
            if key == 'user_id':
                inOutThing.user_id = modify_info[key]
            elif key == 'number':
                inOutThing.number = modify_info[key]
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False
    
def delete(record_id):
    try:
        inOutThing=InOutThing.query.filter_by(record_id=record_id).first()
        db.session.delete(inOutThing)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False