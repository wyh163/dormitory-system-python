from flask import Flask
from app import config
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_login import LoginManager

app = Flask(__name__)
app.debug = True
app.secret_key = 'router'
app.config.from_object(config)

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='/'
login_manager.session_protection='strong'
login_manager.login_message='请先登录注册'

handler=logging.FileHandler('app.log',encoding='UTF-8')
logging_format=logging.Formatter('%(asctime)s-%(levelname)s    %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)

from app import models
from app import controller
from sqlalchemy_utils import create_database, database_exists
def createTable():
    engine=models.db.get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
        models.db.create_all()
        models.Role.initRole()
        models.User.insert(name='Admin', account='admin', password='admin666', \
            role_id=models.Role.RoleName.Admin, phone='112121221', _class='No', school='No')

    # else:
    #     models.db.create_all()
        

createTable()