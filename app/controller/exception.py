#--coding:utf-8--
from flask import Flask, request, jsonify
from app import app
from werkzeug.exceptions import HTTPException
import json

class APIException(HTTPException):
    code = 500
    description="The server encountered an unexpected condition that prevented it from fulfilling the request."
    name="Internal Server Error"

    def __init__(self,code=None,description=None,name=None):
        if code:
            self.code=code
        if description:
            self.description=description
        if name:
            self.name=name
        super(APIException, self).__init__(description,None)

    def get_body(self,environ=None):
        body = dict(
            code = self.code,
            name=self.name,
            request=request.method+' '+self.get_url_no_parm(),
        )
        text=json.dumps(body,sort_keys=False,ensure_ascii=False)
        return text

    def get_headers(self,environ=None):
        return [('Content-Type','application/json')]

    @staticmethod
    def get_url_no_parm():
        full_path=str(request.path)
        return full_path


class RoleInitialError(APIException):
    code=601
    name="Initial database failed."
    description="Internal server error. SQL initialization error"

class ServerError(APIException):
    code=500
    name="Internal Server Error"
    description="Internal Server Error"

@app.errorhandler(Exception)
def framework_error(e):
    app.logger.exception("info: %s" % e)
    if isinstance(e,APIException):
        return e
    if isinstance(e,HTTPException):
        code=e.code
        description=e.description
        return APIException(code=code,description=description)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e

