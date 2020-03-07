from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
import jwt
import json
from werkzeug.security import safe_str_cmp
from modules.helpers.database import db_session

class UserJWT(object):
    
    def __init__(self, arg):
        
        self.arg = arg
        self.email = self.arg["email"]
        self.pwd = self.arg["pwd"]
      
    def UserJWTData(self):
        query = "CALL spGetUserAccount('"+self.email+"')"
        data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]

        encoded = jwt.encode({'data':data}, 'SECRETNI', algorithm='HS256')
        print("---- Encode ", encoded)
        
        return encoded