
import json
import os
from functools import wraps
from flask import request, jsonify

from modules.helpers.database import db_session
from modules.helpers.statuscode import Status
#from modules.helpers.serialize import *
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def insert_category():
 
    formData = request.get_json()
    category_name = formData['category_name']

    query = "CALL spInsertCategory('" +category_name+ "')"
    db_session.execute(query)
    status = Status('200', 'Successfully Added New Category!')
    return status.status_code()

def insert_subcategory():

    formData = request.get_json()
    subCategory_name    = formData['subcategoryname']
    details             = formData['details']
    image_name          = formData['image']
    categoryid          = formData['categoryid']

    query = "CALL spInsertSubCategory('"+subCategory_name+"','"+details+"','"+image_name+"','"+categoryid+"')"
    db_session.execute(query)

    status = Status('200', 'Successfully Added New Category!')
    return status.status_code()

def get_all_category():
    query   = "CALL spGetAllCategory()"
    data    = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    return Status('200', 'Ok', data).status_code()

def get_all_subcategory():
    query   = "CALL spGetAllSubCategory()"
    data    = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    return Status('200', 'Ok', data).status_code()