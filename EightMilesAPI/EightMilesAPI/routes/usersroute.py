
from flask import Blueprint, request

from flask_sqlalchemy import get_debug_queries

from modules.controller.userscontroller import *
from modules.helpers.decorators import token_required
from modules.helpers.userJWTGen import *

usersapi = Blueprint('usersapi', __name__)

@usersapi.route('users/login', methods=['POST'])
def user_login():
    
    json_input = request.json 
    print("------ xxxx ", json_input)
    user = UserJWT(json_input)
    res = UserJWT.UserJWTData(user)
    return res

@usersapi.route('users/new', methods=['POST'])
def create_user():
    return new_user()

@usersapi.route('users/', methods=['GET'])
#@token_required
def get_users():
    #def get_users(current_user):
    return get_all_users()

@usersapi.route('users/<id>', methods=['GET', 'POST'])
#@token_required
def get_single_user_and_update(id):
    #def get_single_user_and_update(current_user,id):
    if request.method == 'POST':
        return update_user_details(id)
    else:
        return get_single_user(id)

@usersapi.route('users/details/<id>', methods=['GET'])
#@token_required
def update_detail(id):
    return get_user_details(id)


def sql_debug(response):
    queries = list(get_debug_queries())
    query_str = ''
    total_duration = 0.0
    for q in queries:
        total_duration += q.duration
        stmt = str(q.statement % q.parameters).replace('\n', '\n       ')
        query_str += 'Query: {0}\nDuration: {1}ms\n\n'.format(stmt, round(q.duration * 1000, 2))

    print('=' * 80)
    print(' SQL Queries - {0} Queries Executed in {1}ms'.format(len(queries), round(total_duration * 1000, 2)))
    print('=' * 80)
    print(query_str.rstrip('\n'))
    print('=' * 80 + '\n')

    return response

usersapi.after_request(sql_debug)