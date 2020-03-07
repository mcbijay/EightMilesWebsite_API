

from flask import Blueprint, request

from flask_sqlalchemy import get_debug_queries

from modules.controller.colorCodeController import *
from modules.helpers.decorators import token_required


colorCodeApi = Blueprint('colorCodeApi', __name__)

@colorCodeApi.route('getAllcolorCode/', methods=['GET'])
def get_all_colorCode():
    return get_all()

@colorCodeApi.route('colorCodeLast/', methods=['GET'])
@token_required
def get_colorCode():
    return get_single_color()

@colorCodeApi.route('color/new', methods=['POST'])
def create_user():
    return insert_color()

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
colorCodeApi.after_request(sql_debug)