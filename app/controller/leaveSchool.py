#--coding:utf-8--
from flask import Flask, request, jsonify,session,flash
from flask import render_template
from app import app,login_manager
from app.models import User
from app.models import Role, LeaveRecord

@app.route('/leaverecord/query', methods=['GET'])
def _query():
    user_id = session.get('_user_id')
    if (User.checkPermission(user_id, Role.Permission.DATA_CENTER_QUERY)):
        records = LeaveRecord.query()
        response = []
        all_users = User.query()
        user_map = {}
        for item in all_users:
            user_map.setdefault(item.user_id, item.name)
        del all_users
        for item in records:
            try:
                response.append({
                    'record_id': item.record_id,
                    'user_id': item.user_id,
                    'name': user_map[item.user_id],
                    'time': item.time,
                    'recorder': item.recorder
                })
            except Exception as e:
                print(e)
                print(item.user_id, item.time, item.recorder)
                return jsonify({'data': 'Exception', 'code': 'Failed'}), 400, {'ContentType':'application/json'}
        return jsonify({'data': response, 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
    return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}

@app.route('/leaverecord/add', methods=['POST'])
def create():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    info = request.json
    student_id = User.getId(info['account'])
    if (student_id is None):
        return jsonify({'data': 'Add Failed. User are not exists.', 'code': 'FAILED'}), 400, {'ContentType':'application/json'}
    LeaveRecord.add(user_id=student_id, time=info['time'], _class=info['class'], recorder = user_id)
    return jsonify({'data': 'Add Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/leaverecord/modify', methods=['POST'])
def modify():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    all_info = request.json
    record_id = all_info['record_id']
    del all_info['record_id']
    LeaveRecord.modify(record_id, all_info)
    return jsonify({'data': 'Update Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/leaverecord/delete', methods=['POST'])
def delete():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    info = request.json
    LeaveRecord.delete(info['record_id'])
    return jsonify({'data': 'Delete Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
