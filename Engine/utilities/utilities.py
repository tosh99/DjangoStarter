import json

from django.db import connection
from django.http import HttpResponse


class DBHelper:
    def fire_db_query(self, query, params):
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


class ResponseHelper:
    def response(self, data=(), code=200, message='OK'):
        resp = {
            'data': data,
            'code': code,
            'message': message
        }

        return HttpResponse(json.dumps(resp))


class Logger:
    def log_error(self, error):
        pass



class EmailHelper:
    def send_email(self):
        pass
