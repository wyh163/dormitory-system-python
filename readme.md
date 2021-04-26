# Environment Requirements
1. install mysql
In Ubuntu.
- download and install mysql
```shell
>>> sudo apt install mysql-server
>>> sudo apt install mysql-client-core-8.0
```

- alter the password for you 

  - change to administor
    ```shell
    >>> sudo su
    ```

  - login to mysql
    ```shell
    >>> mysql
    ```

  - select correspondance database.
    ```
    >>> use mysql
    ```

  - change your password
    ```shell
    >>> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin666';
    >>> flush privileges;
    >>> exit;
    ```

  - exit adminstor role
    ```shell
    >>> exit
    ```

In windows. refer to:
https://www.runoob.com/w3cnote/windows10-mysql-installer.html


2. install python

3. install venv

4. install flask
```shell
>>> pip install flask
```

5. install requirements
```shell
>>> pip install -r requirements.txt
```

6. start the flask
- login mysql to create databases
```shell
>>> mysql -uroot -p
>>> admin666 [password]
>>> create database dormitory_db default character set utf8;
>>> exit;
```
- start the flask app
```shell
>>> export FLASK_APP=run.py
>>> flask run
```

7. API refered to [api.md](./api.md)