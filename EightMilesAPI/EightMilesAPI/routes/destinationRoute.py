
from flask import Blueprint, request

from flask_sqlalchemy import get_debug_queries

from modules.controller.destinationController import *
from modules.helpers.decorators import token_required
from modules.helpers.userJWTGen import *

destinationapi = Blueprint('destinationapi', __name__)

@destinationapi.route('destination/categorynew', methods=['POST'])
def create_destCategory():
    return insert_category()

@destinationapi.route('destination/subcategorynew', methods=['POST'])
def create_destSubCategory():
    return insert_subcategory()

@destinationapi.route('destination/', methods=['GET'])
def get_category():
    return get_all_category()

@destinationapi.route('destination/allsubcategory', methods=['GET'])
def get_subcategory():
    return get_all_subcategory()

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

destinationapi.after_request(sql_debug)