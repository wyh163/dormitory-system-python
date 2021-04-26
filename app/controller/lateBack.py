#--coding:utf-8--
from flask import Flask, request, jsonify,session,flash
from flask import render_template
from app import app,login_manager
from app.models import User
from app.models import Role, LateBack
@app.route('/lateback/add', methods=['POST'])
def lateback_add():
    user_id = session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}
    lateback_info = request.json
    account = lateback_info['account']
    student_user_id = User.getId(account)
    time = lateback_info['time']
    LateBack.add(user_id=student_user_id, time=time, recorder=user_id)
    return jsonify({'data': 'Add success', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/lateback/query', methods=['GET'])
def lateback_query():
    user_id = session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.DATA_CENTER_QUERY)):
        return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}
    data = LateBack.query()
    res = []
    all_users = User.query()
    user_map = {}
    for item in all_users:
        user_map.setdefault(item.user_id, item.name)
    for item in data:
        res.append({
            'id': item.id,
            'name': user_map[item.user_id],
            'time': item.time,
            'recorder': user_map[item.recorder]
        })
    return jsonify({'data': res, 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/lateback/modify', methods=['POST'])
def lateback_modify():
    user_id = session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}
    modify_info = request.json
    id = modify_info['id']
    del modify_info['id']
    account = modify_info['account']
    user_id = User.getId(account)
    del modify_info['account']
    modify_info.setdefault('user_id', user_id)
    result = LateBack.modify(id, modify_info)
    if result[0]:
        return  jsonify({'data': 'Modify success', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
    else:
        return jsonify({'data': f'Modify failed: {result[1]}', 'code': 'FAILED'}), 400, {'ContentType':'application/json'}

@app.route('/lateback/delete', methods=['POST'])
def lateback_delete():
    user_id = session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}
    id = request.json['id']
    result = LateBack.delete(id)
    if result[0]:
        return  jsonify({'data': 'Delete success', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
    else:
        return jsonify({'data': f'Delete failed: {result[1]}', 'code': 'FAILED'}), 400, {'ContentType':'application/json'}

