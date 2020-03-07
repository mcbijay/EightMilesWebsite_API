# Authorization: Bearer {token}
from flask import Blueprint, Flask, request, jsonify, make_response, abort
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
# from modules.models.core import *
from modules.helpers.statuscode import Status
from routes.usersroute import *
from modules.controller.userscontroller import  *

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):  
        if not 'Authorization' in request.headers:
            return Status('404', 'Token Not Found!').status_code()
        
        current_user = None
        data = request.headers['Authorization']
        token = str.replace(str(data),'Bearer','')
        tok   = str.replace(str(token),' ','') 
        try:
            data = jwt.decode(tok,'SECRETNI', algorithms=['HS256'])
            print("--------------- decode", data)
        except:
            return Status('404', 'Token Not Found!').status_code()
        return f(current_user, *args, **kwargs)
    return decorated

