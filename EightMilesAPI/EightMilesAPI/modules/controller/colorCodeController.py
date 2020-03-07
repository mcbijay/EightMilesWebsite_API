import json
import os
from functools import wraps
from flask import request, jsonify

#from modules.helpers.database import db_session
#from modules.helpers.statuscode import Status
#from modules.helpers.serialize import *
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def get_all():
    query = "CALL spGetAllColorCode()"
    data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    return Status('200', 'Ok', data).status_code()

def get_single_color():
    query = "CALL spGetColorCode()"
    data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    return Status('200', 'Ok', data).status_code()

def insert_color():

    if request.method == 'POST':
        file = request.files['file']
        name = request.form['colorName']
        print(file.filename, " ----------------- ", name)
        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)
            query = "call spInserColor('"+name+"','"+file.filename+"')"
            db_session.execute(query)
            file.save("./static/images/"+ filename)
            
    status = Status('200', 'Successfully Added New Color!')
    return status.status_code()
    