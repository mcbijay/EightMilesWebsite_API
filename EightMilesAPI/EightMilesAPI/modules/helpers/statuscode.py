
from flask import jsonify

class Status(object):

    def __init__(self, code, msg, data=None):
        self.code   = code
        self.msg    = msg
        self.data   = data
    
    def status_code(self):
        res = {}
        res['code'] = self.code
        res['msg']  = self.msg
        res['data'] = self.data

        return jsonify(res)