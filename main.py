#install peewee
from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Samtravels.db"))

#creating our table
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

User.create_table(fail_silently=True)



class Student(Model):
    stud_name = CharField()
    stud_id = CharField(unique=True)
    stud_stream = CharField()

    class Meta:
        database = db

Student.create_table(fail_silently=True)