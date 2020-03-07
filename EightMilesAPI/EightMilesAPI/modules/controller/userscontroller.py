import json

from functools import wraps
from flask import request, jsonify

from modules.helpers.database import db_session
from modules.helpers.statuscode import Status
from modules.helpers.serialize import *
from modules.model.usersmodel import *

"""
Create API function here
"""

def escapestring(str):
    return str.replace("'","''")

def new_user():

    formData = request.get_json()
    email = formData['email']
    pasw = formData['pwd']
    usertype = formData['usrtypeID']
    print("------  ", formData)
    is_exist = Users.query.filter_by(email=email).first()
    if not is_exist:
        query = "CALL spInserUser('" +email+ "','" +escapestring(pasw)+ "','" +usertype+ "')"
        try:
            db_session.execute(query)
            status = Status('200', 'Successfully Added New User!')
            return status.status_code()
        except:
           return Status('203', 'Something went wront, pls try again later!').status_code()
    else:
        return Status('204', 'User already exist!').status_code()
   
    
def get_single_user(id):
    user = Users.query.filter_by(user_id=id).first()
    data = serialize_data(user)

    if user:
        return Status('200', 'Ok', data).status_code()   
    else:
        return Status('404', 'User not found!').status_code()

def get_all_users():

    query = "CALL spUsers()"
    data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    return Status('200', 'Ok', data).status_code()

def get_user_details(id):
    query = "CALL spGetUserDetails("+id+")"
    data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    
    if data:
        return Status('200', 'Ok', data).status_code()        
    else:
        return Status('404', 'Ok').status_code()

def update_user_details(id):
    user_detail = UserDetails.query.get(id)
    data = serialize_detail(user_detail)
  
    return ''

def delete_user():
    return ''
