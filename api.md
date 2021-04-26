1. user register: `$url:$port/user/register`

parameters: 
```python
{
    'name': name, 
    'account': account, 
    'password': pwd
}
```
return:
```python
jsonify({'data':'成功注册','code':'SUCCESS'}),200,{"ContentType":"application/json"}
```

2. user login: `$url:$port/user/login`

parameters:
```python
{
    'account': account, 
    'password': pwd
}
```
return like user register

3. get register list: `$url:$port/user/getCheckList`

Parameters: No.

return: 
```python
[
    {
        'name': item.name,
        'user_id': item.user_id,
        'account': item.account
    }
]
```

4. check register list: `$url:$port/user/updateCheckList`

parameters:
```python
{
    'user_id': user_id,
    'passed': True or False
}
```
return:
```python
jsonify({'data': 'Update Successfully', 'code': 'SUCCESS'}), 200, {'ContentType': 'application/json'}
```

5. add leave school record: `/leaverecord/add`

parameter:
```python
{
    'account': 'hua_yan_tsn',
    'time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M'),
    'class': 'grade 2 class 1'
}
```

return like check register list

6. query leave school record: `/leaverecord/query`

parameters: No.

return: 
```python
[
    {
        'record_id': item.record_id,
        'user_id': item.user_id,
        'name': user_map[item.user_id],
        'time': item.time
    }
]
```

7. modify leave school record: `/leaverecord/modify`

parameters: 
```python
{
    record_id: record_id
}
```

return like check register list.

8. delete leave school record: `/leaverecord/delete`

parameters:
```python
{
    record_id: record_id
}
```

return like check register list.

9. query in out thing: `/inoutthing/query`

paramters: No.

return: 
```python
{
    'record_id': item.record_id,
    'user_id': item.user_id,
    'name': user_map[item.user_id],
    'number': item.number
}
```

10. add in out thing: `/inoutthing/add`

parameters:
```python
{
    'account': 'hua_yan_tsn',
    'number': 3
}
```

return like check register list.

11. modify in out thing:  `/inoutthing/modify`

parameters:
```python
{
    'record_id': data[0]['record_id'],
    'number': 2
}
```

return like check register list.


12. delete in out thing:  `/inoutthing/delete`

parameters:
```python
{
    'record_id': data[0]['record_id']
}
```

return like check register list.

13. add lateback record: `/lateback/add`
```python
    api = '/lateback/add'
    current = datetime.datetime.today()
    payload = {
        'account': 'MG1937028',
        'time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M')
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)
```

14. query lateback record: `/lateback/query`
```python
    api = '/lateback/query'
    response = session.get(f'{base_url}{api}')
    print(response.text)
```

15. modify lateback record: `/lateback/modify`
```python
    id = json.loads(response.text)['data'][0]['id']
    api = '/lateback/modify'
    payload = {
        'id': id,
        'account': 'admin',
        'time': datetime.datetime.strftime(current, '%Y-%m-%d %H:%M')
    }
    response = session.post(f'{base_url}{api}', json=payload)
    print(response.text)
```

16. Delete lateback record: `/lateback/delete`
```python
    api = '/lateback/delete'
    response = session.post(f'{base_url}{api}', json={'id': id})
    print(response.text)
```

17. Add checkin record: `/checkin/add`
```python
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
```

18. Query all checkin record: `/checkin/queryall`
```python
    api = '/checkin/queryall'
    response = session.get(f'{base_url}{api}')
    print(response.text)
```

19. Query checkin by id: `/checkin/querybyid`
```python
    id = json.loads(response.text)['data'][0]['id']
    api = '/checkin/querybyid'
    response = session.get(f'{base_url}{api}', json={'id': id})
```

20. Modify checkin info: `/checkin/modify`
```python
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
```
    
21. Delete lateback record: `/checkin/delete`
```python
    api = '/checkin/delete'
    response = session.post(f'{base_url}{api}', json={'id': id})
```