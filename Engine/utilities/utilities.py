import json

from django.db import connection
from django.http import HttpResponse


def generic_database_connect(query, params):
    try:
        for key, value in params.items():
            value = str(value).replace("'", "''")
            query = query.replace(key, str(value))
    except:
        pass

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except:
        pass


def response(data=(), code=200, message='OK'):
    resp = {
        'data': data,
        'code': code,
        'message': message
    }

    return HttpResponse(json.dumps(resp))
