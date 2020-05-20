from sqlalchemy import create_engine, Column, ForeignKey, func
from sqlalchemy import Integer, String, Float, DECIMAL, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
import random
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table
# localhost


HOSTNAME = '127.0.0.1'
DATABASE = 'demo0424'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    city = Column(String(50))
    age = Column(Integer)

    def __str__(self):
        return "User{username: %s}" % self.username

# Base.metadata.drop_all()
Base.metadata.create_all()

session = sessionmaker(bind=engine)()

# 查询和王同学相同城市和年龄的

# user = session.query(User).filter(User.username == 'wang').first()
# print(user.city)
# print(user.age)
#
# result = session.query(User).filter(User.city == user.city, User.age == user.age)
# for data in result:
#     print(data)

# 子查询 label 重新命名
# sub = session.query(User.city.label('city'), User.age.label('age')).filter(User.username == 'wang').subquery()

# c column
# result = session.query(User).filter(User.city == sub.c.city, User.age == sub.c.age)
# print(result)
# for data in result:
#     print(data)









