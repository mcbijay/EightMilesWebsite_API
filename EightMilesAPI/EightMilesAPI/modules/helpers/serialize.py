from flask import jsonify

def serialize_data(self):
    return {
        'email':self.email,
        'pwd': self.pwd,
        'detail_id': self.details[0].detail_id
    }

def serialize_detail(self):
    return {
        "fname":self.fname,
        "lname":self.lname,
        "mobile":self.mobile,
        "telno":self.telno,
        "address":self.address,
        # "profile_image":self.profile_image,
        "user_id": self.user_id,
        # "type_id": self.type_id,
        # "status_id": self.status_id
    }