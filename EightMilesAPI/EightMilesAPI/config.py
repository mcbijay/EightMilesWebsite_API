
from flask import Flask
import os


ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'modules')
SESSION_PATH = os.path.join(ROOT_PATH, 'sessions')

ENV = 'dev'
ENVIRONMENT = {
    'dev':{
        #mysql
        'DBHOST' : '127.0.0.1:3306',
        'DBNAME' : 'eightmiles_website',
        'DBUSER' : 'root',
        'DBPASS' : ''
    },
    'prod':{
        'DBHOST' : '127.0.0.1:3306',
        'DBNAME' : '',
        'DBUSER' : '',
        'DBPASS' : ''
    }
}
#HOST = {'HOST':'127.0.0.1', 'PORT':3000}
DBNAME = ENVIRONMENT[ENV]['DBNAME']
DBHOST = ENVIRONMENT[ENV]['DBHOST']
DBUSER = ENVIRONMENT[ENV]['DBUSER']
DBPASS = ENVIRONMENT[ENV]['DBPASS']

SESSION_OPTS = {
    'session.type'              : 'file',
    'session.cookie_expires'    : True,
    'session.timeout'           : 900,
    'session.auto'              : True,
    'session.url'               : 'mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8mb4'.format(DBUSER, DBPASS, DBHOST, DBNAME),
    'session.lock_dir'          : os.path.join(SESSION_PATH, 'locks'),
    'session.data_dir'          : os.path.join(SESSION_PATH, 'data')
}