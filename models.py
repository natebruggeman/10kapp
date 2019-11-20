from peewee import *

from flask_login import UserMixin


DATABASE = SqliteDatabase('skills.sqlite')


class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()

    class Meta:
        database = DATABASE



class Skill(Model):
    goal = CharField()
    objective = CharField()
    time = IntegerField()
    

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Skill], safe=True)
    print("Tables Created")
    DATABASE.close()