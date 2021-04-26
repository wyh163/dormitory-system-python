#--coding:utf-8--
from flask import Flask, request, jsonify,session,flash
from flask import render_template
from app import app,login_manager
from app.models import User
from app.models import Role, Thing

@app.route('/inoutthing/query', methods=['GET'])
def inoutthing_find():
    user_id = session.get('_user_id')
    if (User.checkPermission(user_id, Role.Permission.DATA_CENTER_QUERY)):
        recs = Thing.query()
        response = []
        all_users = User.query()
        user_map = {}
        for item in all_users:
            user_map.setdefault(item.user_id, item.name)
        del all_users

        for item in recs:
            response.append({
                'record_id': item.record_id,
                'user_id': item.user_id,
                'name': user_map[item.user_id],
                'number': item.number
            })
        return jsonify({'data': response, 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
    return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}

@app.route('/inoutthing/add', methods=['POST'])
def inoutthing_create():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    info = request.json
    user_id = User.getId(info['account'])
    Thing.add(user_id = user_id, number = info['number'])
    return jsonify({'data': 'Add Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/inoutthing/modify', methods=['POST'])
def inoutthing_modify():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    all_info = request.json
    record_id = all_info['record_id']
    del all_info['record_id']
    Thing.modify(record_id, all_info)
    return jsonify({'data': 'Update Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/inoutthing/delete', methods=['POST'])
def inoutthing_delete():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    info = request.json
    Thing.delete(info['record_id'])
    return jsonify({'data': 'Delete Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
