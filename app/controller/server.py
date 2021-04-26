#--coding:utf-8--
from flask import Flask, request, jsonify
from flask import render_template
from app import app
from app.models import User,Privillege,Role

# @app.route('/')
# @app.route('/index')
# def index():
#     User.createTable()
#     Role.initRole()
#     return render_template('index.html')


# @app.route('/add', methods=['GET','POST'])
# def add():
#     print(request.headers)
#     print(type(request.json))
#     print(request.json)
#     result = request.json['a'] + request.json['b']
#     return str(result)

# @app.route('/test', methods=['GET'])
# def test():
#     return jsonify({'data':'HI~william!', 'code':'SUCCESS'}), 200, {"ContentType":"application/json"}

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
