from django.db import connection
from contextlib import closing

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns , row)) for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    col = [col[0] for col in cursor.description]
    return dict(zip(col , row))


def get_books():
    with closing(connection.cursor()) as cursor:
        cursor.execute('''SELECT * FROM my_app_book''')
        books = dictfetchall(cursor)
        return books

def get_users():
    with closing(connection.cursor()) as cursor:
        cursor.execute('''SELECT * FROM auth_user''')
        users = dictfetchall(cursor)
        return users
