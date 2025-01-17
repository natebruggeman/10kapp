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
    owner = ForeignKeyField(User, backref='skills')
    objective = CharField()
    time = IntegerField()

    

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Skill], safe=True)
    print("Created tables if they weren't already there")
    DATABASE.close()