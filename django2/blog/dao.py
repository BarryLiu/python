from django.db import connection

cursor = connection.cursor()

connection.commit()