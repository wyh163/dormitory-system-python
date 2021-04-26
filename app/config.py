#--coding:utf-8--
#! user/bin/python
DEBUG = True

# db相关
DIALCT = 'mysql'
DRIVER = "pymysql"
USERNAME = 'root'
PASSWORD = 'admin666'
HOST = '127.0.0.1'
PORT = '3306'
DBNAME = 'dormitory_db'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALCT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True   

