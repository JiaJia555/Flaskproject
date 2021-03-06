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
DATABASE = 'demo0422'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)


class User(Base):
    __tablename__ = "user2"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    gender = Column(Enum('男', '女'))
    age = Column(Integer)


# Base.metadata.drop_all()
Base.metadata.create_all()
session = sessionmaker(bind=engine)()

# for x in range(10):
#     user = User(username= 'futongxue%s' % x, gender='男', age=random.randint(10, 25))
#     session.add(user)
#
# session.commit()


# 按照性别分组 并求和 聚合函数
# result = session.query(User.gender, func.count(User.id)).group_by(User.gender).all()


# having
# result = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age<18).all()
# print(result)

# join
# https://blog.csdn.net/zhengsy_/article/details/90733864