
import json
import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from modules.helpers.database import Base

class Users(Base):
    __tablename__ = 'usersaccount'
    user_id = Column(Integer, primary_key=True)
    email   = Column(String(255))
    pwd     = Column(String(255))
    usertypeID = Column(String(255))

    #details = relationship('UserDetails', backref='details')

class UserType(Base):
    __tablename__ = 'userstype'
    usrtype_id  = Column(Integer, primary_key=True)
    #usrtype     = Column(Integer)
    userTypeName        = Column(String(255))

class UserStatus(Base):
    __tablename__ = 'userstatus'
    status_id   = Column(Integer, primary_key=True)
    status      = Column(Integer)
    desc        = Column(String(255))

class UserDetails(Base):
    __tablename__ = 'userdetails'
    detail_id       = Column(Integer, primary_key=True)
    fname           = Column(String(255))
    lname           = Column(String(255))
    mobile          = Column(String(255))
    telno           = Column(String(255))
    address         = Column(String(255))
    #profile_image   = Column(String(255))

    user_id     = Column(Integer, ForeignKey('usersaccount.user_id'))
    type_id     = Column(Integer, ForeignKey('userstype.usrtype_id'))
#    status_id   = Column(Integer, ForeignKey('userstatus.status_id'))
