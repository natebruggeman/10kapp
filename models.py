from peewee import *

DATABASE = SqliteDatabase('skills.sqlite')


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