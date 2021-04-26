#--coding:utf-8--
from flask import Flask, request, jsonify,session,flash
from flask import render_template
from app import app,login_manager
from app.models import User
from app.models import Role
from app.models import Privillege
from flask_login import logout_user,current_user,login_required,login_user

@login_manager.user_loader
def load_user(user_id):
    return User.retrieve(user_id)

@app.route('/user/login',methods=['POST','GET'])
def login():
    acct=request.json['account']
    pwd=request.json['password']
    user_id=User.getId(acct)
    if user_id ==None:
        return jsonify({'data':'账号不存在','code':'FAILED'}),300,{"ContentType":"application/json"}
    user=User.checkLogin(user_id,pwd)
    if user:
        login_user(user,remember=True)
        return jsonify({'data':'成功登录','code':'SUCCESS'}),200,{"ContentType":"application/json"}
    else:
        return jsonify({'data':'账号或密码错误','code':'FAILED'}),303,{"ContentType":"application/json"}


@app.route('/user/register',methods=['POST'])
def register():
    if User.insert(name=request.json['name'],account=request.json['account'],password=request.json['password'],role_id=Role.RoleName.Register, \
        phone=request.json['phone'], _class=request.json['class'], school=request.json['school']):
        return jsonify({'data':'成功注册','code':'SUCCESS'}),200,{"ContentType":"application/json"}
    else:
        return jsonify({'data':'账号已存在','code':'FAILED'}),200,{"ContentType":"application/json"}
				

@app.route('/user/resetPwd',methods=['POST'])
def resetPwd():
    user_id=session.get('_user_id')
    if user_id ==None:
        return jsonify({'data':'未登录','code':'FAILED'}),200,{"ContentType":"application/json"}
    old_pwd=request.json['oldpwd']
    new_pwd=request.json['newpwd']
    if User.checkLogin(user_id,old_pwd):			
        if User.update(user_id,new_pwd):
            return jsonify({'data':'重置密码成功','code':'SUCCESS'}),200,{"ContentType":"application/json"}
        else:
            return jsonify({'data':'密码重置失败','code':'FAILED'}),200,{"ContentType":"application/json"}
    else:
        return jsonify({'data':'旧密码错误','code':'FAILED'}),200,{"ContentType":"application/json"}


@app.route('/user/forgotPwd',methods=['POST'])
def forgotPwd():
    acct=request.json['account']
    user_id=User.getId(acct)
    if user_id == None:
        return jsonify({'data':'账号不存在','code':'FAILED'}),200,{"ContentType":"application/json"}
    new_pwd=request.json['password']		
    if User.update(user_id,new_pwd):
        return jsonify({'data':'重置密码成功','code':'SUCCESS'}),200,{"ContentType":"application/json"}
    else:
        return jsonify({'data':'密码重置失败','code':'FAILED'}),200,{"ContentType":"application/json"}
	

@app.route("/user/logout",methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'data':'登出','code':'SUCCESS'}),200,{"ContentType":"application/json"}


@app.route("/user/getInfo",methods=['GET'])
@login_required
def getInfo():
    user_id=session.get('_user_id')
    if user_id == None:
        return jsonify({'name':'未登录','account':'暂无', 'role_id':'暂无'}),200,{"ContentType":"application/json"}
    the_user=User.retrieve(user_id)
    name = the_user.name
    account = the_user.account
    role_id = the_user.role_id
    role_name = Role.getRoleName(role_id)
    _class = the_user._class
    phone = the_user.phone
    school = the_user.school
    return jsonify({'name':name, 'account':account, \
            'role_name':role_name, 'class':_class, \
                'phone':phone, 'school':school}),200,{"ContentType":"application/json"}


@app.route("/user/getInfo/editName",methods=['POST'])
@login_required
def editName():
    user_id=session.get('_user_id')
    if user_id == None:
        return jsonify({'data':'未登录','code':'FAILED'}),200,{"ContentType":"application/json"}
    name = request.json['name']
    if User.updateName(user_id,name):
        return jsonify({'data':'修改昵称成功','code':'SUCCESS'}),200,{"ContentType":"application/json"}
    else:
        return jsonify({'data':'修改昵称失败','code':'FAILED'}),200,{"ContentType":"application/json"}


@app.route("/user/getInfo/editIntroduction",methods=['POST'])
@login_required
def editIntroduction():
    user_id=session.get('_user_id')
    if user_id == None:
        return jsonify({'data':'未登录','code':'FAILED'}),200,{"ContentType":"application/json"}
    introduction = request.json['introduction']
    if User.updateIntroduction(user_id,introduction):
        return jsonify({'data':'修改信息成功','code':'SUCCESS'}),200,{"ContentType":"application/json"}
    else:
        return jsonify({'data':'修改信息失败','code':'FAILED'}),200,{"ContentType":"application/json"}

@app.route("/user/getCheckList", methods=['GET'])
@login_required
def getCheckList():
    user_id = session.get('_user_id')
    if user_id == None:
        return jsonify({'data':'未登录','code':'FAILED'}),400,{"ContentType":"application/json"}
    if not User.checkPermission(user_id, Role.Permission.USER_CENTER_QUERY):
        return jsonify({'data': 'Permission Limited', 'code': 'FAILED'}), 300, {'ContentType': 'application/json'}
    all_record = User.query()
    registers = list(filter(lambda item: item.role_id==Role.RoleName.Register, all_record))
    response = []
    for item in registers:
        try:
            response.append({
                'name': item.name,
                'user_id': item.user_id,
                'account': item.account
            })
        except Exception as e:
            print(e)
            print(item)
            return jsonify({'data': 'Query Failed', 'code': 'FAILED'}), 400, {'ContentType': 'application/json'}
    return jsonify({'data': response, 'code': 'SUCCESS'}), 200, {'ContentType': 'application/json'}


@app.route("/user/updateCheckList", methods=['POST'])
@login_required
def updateCheckList():
    user_id = session.get('_user_id')
    if user_id == None:
        return jsonify({'data':'未登录','code':'FAILED'}),400,{"ContentType":"application/json"}
    if not User.checkPermission(user_id, Role.Permission.MODIFY):
        return jsonify({'data': 'Permission Limited', 'code': 'FAILED'}), 300, {'ContentType': 'application/json'}
    info = request.json
    passed = info['passed']
    uid = info['user_id']
    if passed:
        User.updateRole(uid, Role.RoleName.User)
    else:
        User.delete(uid)
    return jsonify({'data': 'Update Successfully', 'code': 'SUCCESS'}), 200, {'ContentType': 'application/json'}

@app.route('/user/delete', methods=['POST'])
def user_delete():
    user_id = session.get('_user_id')
    if not User.checkPermission(user_id, Role.Permission.MODIFY):
        return jsonify({'data': 'Permission Limited', 'code': 'FAILED'}), 300, {'ContentType': 'application/json'}
    uid = request.json['user_id']
    User.delete(uid)
    return jsonify({'data': 'Delete Successfully', 'code': 'SUCCESS'}), 200, {'ContentType': 'application/json'}