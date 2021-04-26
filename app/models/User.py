#--coding:utf-8--
from app.models import db
from werkzeug.security import generate_password_hash,check_password_hash
from app.models import Role, LeaveRecord, Thing
from flask_login import UserMixin


class User(db.Model):
    __tablename__='users'
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    name=db.Column(db.String(20),nullable=False) 
    account=db.Column(db.String(20),nullable=False,unique=True)
    _password=db.Column(db.String(128),nullable=False)
    role_id=db.Column(db.Integer)
    phone=db.Column(db.String(11), nullable=False)
    _class=db.Column(db.String(20), nullable=False)
    school = db.Column(db.String(20), nullable=False)

              
    @property
    def password(self):
         return self._password

    @password.setter
    def password(self,passw):
        self._password=generate_password_hash(passw)
    
    def checkPassword(self,passw):
        return check_password_hash(self._password,passw)

    def __init__(self,**kwargs):
        super(User,self).__init__(**kwargs)
    
    def __repr__(self):
        return '<User: %r >' % (self.account)

    def can(self,permissions):
        return (self.role_id is not None) and (Role.getPermission(self.role_id) in [255, permissions])

    @staticmethod
    def get(user_id):
        pass

    def is_authenticated(self):#TODO
        return True

    def is_active(self):#TODO
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

def insert(**kwargs):
    try:
        user=User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False


def query():
    res=User.query.all()
    return res


def update(uid,pwd):
    try:
        user=User.query.filter_by(user_id=uid).first()
        user.password=pwd
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def updateName(uid,name):
    try:
        user=User.query.filter_by(user_id=uid).first()
        user.name=name
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def updateRole(uid, role_id):
    try:
        user=User.query.filter_by(user_id=uid).first()
        user.role_id=role_id
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def delete(uid):
    try:
        use=User.query.filter_by(user_id=uid).first()
        db.session.delete(use)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False
    

def checkLogin(uid,passw):    
    data=User.query.filter_by(user_id=uid).first()
    if data is not None and data.checkPassword(passw):
        return data
    else:
        return None

def checkPermission(uid,permissions):
    use=User.query.filter_by(user_id=uid).first()
    return use.can(permissions)

def getId(acct):
    data=User.query.filter_by(account=acct).first()
    if data ==None:
        return None
    return data.get_id()

def retrieve(uid):
    the_user = User.query.filter_by(user_id=uid).first()
    return the_user
