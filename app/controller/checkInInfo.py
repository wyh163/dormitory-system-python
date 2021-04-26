#--coding:utf-8--
from flask import Flask, request, jsonify,session,flash
from flask import render_template
from app import app,login_manager
from app.models import User
from app.models import Role, CheckInInfo

@app.route('/checkin/queryall', methods=['GET'])
def checkin_find():
    user_id = session.get('_user_id')
    if (User.checkPermission(user_id, Role.Permission.DATA_CENTER_QUERY)):
        recs = CheckInInfo.query_all()
        response = []
        all_users = User.query()
        user_map = {}
        for item in all_users:
            user_map.setdefault(item.user_id, item.name)
        del all_users

        for item in recs:
            response.append({
                'id': item.id,
                'user_id': item.user_id,
                'checkin_time': item.checkin_time,
                'checkout_time': item.checkout_time,
                'checkin_recorder': item.checkin_recorder,
                'checkout_recorder': item.checkout_recorder,
                'checkin_things': item.checkin_things
            })
        return jsonify({'data': response, 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
    return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}


@app.route('/checkin/querybyid', methods=['GET'])
def checkin_query_by_id():
    user_id = session.get('_user_id')
    if (User.checkPermission(user_id, Role.Permission.DATA_CENTER_QUERY)):
        recs = CheckInInfo.query(request.json['id'])
        if recs is None:
            return jsonify({'data': 'No such records', 'code': 'Failed'}), 400, {'ContentType':'application/json'}
        all_users = User.query()
        user_map = {}
        for item in all_users:
            user_map.setdefault(item.user_id, {'name': item.name, 'account': item.account})
        del all_users
        response = {
            'id': recs.id,
            'account': user_map[item.user_id]['account'],
            'name': user_map[item.user_id]['name'],
            'checkin_time': recs.checkin_time,
            'checkout_time': recs.checkout_time,
            'checkin_recorder': recs.checkin_recorder,
            'checkout_recorder': recs.checkout_recorder,
            'checkin_things': recs.checkin_things
        }
        return jsonify({'data': response, 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
    return jsonify({'data': 'Permission Denied', 'code': 'Failed'}), 300, {'ContentType':'application/json'}


@app.route('/checkin/add', methods=['POST'])
def checkin_create():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    info = request.json
    user_id = User.getId(info['account'])
    CheckInInfo.add(user_id = user_id, checkin_time=info['checkin_time'],\
        checkout_time = info['checkout_time'], checkin_recorder = info['checkin_recorder'],\
        checkout_recorder = info['checkout_recorder'],\
        checkin_things = info['checkin_things'])
    return jsonify({'data': 'Add Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/checkin/modify', methods=['POST'])
def checkin_modify():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    all_info = request.json
    id = all_info['id']
    del all_info['id']
    CheckInInfo.modify(id, all_info)
    return jsonify({'data': 'Update Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}

@app.route('/checkin/delete', methods=['POST'])
def  checkin_delete():
    user_id=session.get('_user_id')
    if (not User.checkPermission(user_id, Role.Permission.MODIFY)):
        return jsonify({'data': 'Permission Denied', 'code': 'FAILED'}), 300, {'ContentType':'application/json'}
    info = request.json
    CheckInInfo.delete(info['id'])
    return jsonify({'data': 'Delete Successfully.', 'code': 'SUCCESS'}), 200, {'ContentType':'application/json'}
