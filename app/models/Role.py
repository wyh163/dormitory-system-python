#--coding:utf-8--
from app.models import db
from app.models import Privillege

class Permission:
    USER_CENTER_QUERY=0x01
    DATA_CENTER_QUERY=0x02
    ADD=0x04
    DELETE=0x08
    MODIFY=0x10

class RoleName:
    Admin=1
    User=2
    Register=3
    PastUser=4

class Role(db.Model):
    __tablename__ = "roles"
    role_id = db.Column(db.INTEGER,primary_key=True)    
    name=db.Column(db.String(20),unique=True)
    dept = db.Column(db.String(100))
    permissions=db.Column(db.Integer)
    
    def __init__(self,**kwargs):
        super(Role,self).__init__(**kwargs)

    @staticmethod
    def insertRoles():
        roles={
            'Admin':(0xff),
            'User':(Permission.DATA_CENTER_QUERY|
                    Permission.DELETE|
                    Permission.MODIFY
                    ),
            'Register': (Permission.USER_CENTER_QUERY),
            'PastUser': (Permission.USER_CENTER_QUERY)
        }
        try:
            for r in roles:
                role=Role.query.filter_by(name=r).first()
                if role is None:
                    role=Role(name=r)
                    role.permissions=roles[r]
                    db.session.add(role)
            db.session.commit()
        except:
            db.session.rollback()


def getPermission(rid):
    role=Role.query.filter_by(role_id=rid).first()
    if role is not None:
        return role.permissions

def initRole():
    Role.insertRoles()

def getRoleName(rid):
    role=Role.query.filter_by(role_id=rid).first()
    if role is not None:
        return role.name
