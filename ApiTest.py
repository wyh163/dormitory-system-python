import requests
import json
import datetime
import time
base_url = "http://127.0.0.1:5000"
# url = "/user/register"
session = requests.session()
def test_user_center():
    print('test register api result: ', end='')
    api = '/user/register'
    payload={
        'name': 'William', 
        'account': 'MG1937028', 
        'password': 'admin666',
        'class': 'grade 1 class 2',
        'phone': '12345678901',
        'school': 'xx university'
    }
    headers = {}
    response = requests.post(f'{base_url}{api}', headers=headers, json=payload)
    print(response.text)
    payload={
        'name': 'William', 
        'account': 'MG1937017', 
        'password': 'admin666',
        'class': 'grade 2 class 3',
        'phone': '12345678911',
        'school': 'xx university'
    }
    headers = {}
    response = requests.post(f'{base_url}{api}', headers=headers, json=payload)


    print('test login api result: ', end='')
    api = '/user/login'
    payload={
        'account': 'admin', 
        'password': 'admin666'
    }
    response = session.get(f'{base_url}{api}', json=payload)
    print(response.text)


    print('test get information of user: ', end='')
    api = '/user/getInfo'
    response = session.get(f'{base_url}{api}')
    print(response.text)

    print('test register query api result: ', end='')
    api = '/user/getCheckList'
    response = session.get(f'{base_url}{api}')
    print(response.text)

    time.sleep(1)
    data = json.loads(response.text)['data']
    print('test register state update api result: ', end='')
    api = '/user/updateCheckList'
    if len(data) != 0:
        for item in data:
            response = session.post(f'{base_url}{api}', json={
                'user_id': item['user_id'],
                'passed': True
            })
        print(response.text)
    else:
        print()
    
    print('test logout api result: ', end='')
    api = '/user/logout'
    response = session.post(f'{base_url}{api}')
    print(response.text)

    print('test user login result: ', end='')
    api = '/user/login'
    payload={
        'account': 'MG1937028', 
        'password': 'admin666'
    }
    response = session.get(f'{base_url}{api}', json=payload)
    print(response.text)

    print('test user logout result: ', end='')
    api = '/user/logout'
    response = session.post(f'{base_url}{api}')
    print(response.text)

    print('test admin user login', end='')
    api = '/user/login'
    payload = {
        'account': 'admin',
        'password': 'admin666'
    }
    response = session.get(f'{base_url}{api}', json=payload)
    print(response.text)

    print('test admin delete user result: ', end='')
    api = '/user/delete'
    response = session.post(f'{base_url}{api}', json={'user_id': 3})
    print(response.text)



def test_leave_school_record():
    print('test add leave school record: ', end='')
    api = '/leaverecord/add'
    current = datetime.datetime.today()
    payload = {
        'account': 'MG1937028',
        'time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M'),
        'class': 'grade 2 class 1'
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)

    print('test query leave school record: ', end='')
    api = '/leaverecord/query'
    response = session.get(f'{base_url}{api}', json=None)
    print(response.text)

    print('test modify leave school record: ', end='')
    api = '/leaverecord/modify'
    data = json.loads(response.text)['data']
    payload = {
        'record_id': data[0]['record_id'],
        '_class': 'grade 3 class 2'
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)

    print('test delete leave school record: ', end='')
    api = '/leaverecord/delete'
    response = session.post(f'{base_url}{api}', json={'record_id': data[0]['record_id']})
    print(response.text)

def test_in_out_thing():
    print('test add in out thing record: ', end='')
    api = '/inoutthing/add'
    payload = {
        'account': 'MG1937028',
        'number': 3
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)

    print('test query in out thing record: ', end='')
    api = '/inoutthing/query'
    response = session.get(f'{base_url}{api}', json=None)
    print(response.text)
    data = json.loads(response.text)['data']

    print('test modify in out thing record: ', end='')
    api = '/inoutthing/modify'
    if len(data) != 0:
        payload = {
            'record_id': data[0]['record_id'],
            'number': 2
        }
        response = session.post(f'{base_url}{api}', json=payload)
        print(response.text)


    print('test delete in out thing record: ', end='')
    api = '/inoutthing/delete'
    response = session.post(f'{base_url}{api}', json={'record_id': data[0]['record_id']})
    print(response.text)

def test_lateback():
    
    print('test add lateback record: ', end='')
    api = '/lateback/add'
    current = datetime.datetime.today()
    payload = {
        'account': 'MG1937028',
        'time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M')
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)


    print('test query lateback record: ', end='')
    api = '/lateback/query'
    response = session.get(f'{base_url}{api}')
    print(response.text)
    
    
    print('test modify lateback record: ', end='')
    id = json.loads(response.text)['data'][0]['id']
    api = '/lateback/modify'
    payload = {
        'id': id,
        'account': 'admin',
        'time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M')
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)
    
    
    print('test delete lateback record: ', end='')
    api = '/lateback/delete'
    response = session.post(f'{base_url}{api}', json={'id': id})
    print(response.text)


def test_checkin():
    print('test add checkin record: ', end='')
    api = '/checkin/add'
    current = datetime.datetime.today()
    payload = {
        'account': 'MG1937028',
        'checkin_recorder': 'Admin',
        'checkout_recorder': 'Admin',
        'checkin_time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M'),
        'checkout_time': None,
        'checkin_things': 'package'
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)


    print('test query all checkin record: ', end='')
    api = '/checkin/queryall'
    response = session.get(f'{base_url}{api}')
    print(response.text)
    
    id = json.loads(response.text)['data'][0]['id']
    print('test query checkin record by id: ', end='')
    api = '/checkin/querybyid'
    response = session.get(f'{base_url}{api}', json={'id': id})
    print(response.text)
    
    print('test modify checkin record: ', end='')
    api = '/checkin/modify'
    payload = {
        'id': id,
        'account': 'MG1937017',
        'checkin_recorder': 'Admin',
        'checkout_recorder': 'Admin2',
        'checkin_time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M'),
        'checkout_time': None,
        'checkin_things': None
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)
    
    
    print('test delete lateback record: ', end='')
    api = '/checkin/delete'
    response = session.post(f'{base_url}{api}', json={'id': id})
    print(response.text)

test_user_center()
test_leave_school_record()
test_in_out_thing()
test_lateback()
test_checkin()