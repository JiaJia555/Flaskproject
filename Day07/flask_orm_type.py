from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, Float, DECIMAL, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Date, DateTime, Time
from datetime import datetime, date, time
from sqlalchemy.dialects.mysql import LONGTEXT
# 第二种写法
# import enum
# class MyEnum(enum.Enum):
#     one = 1
#     two = 2
#     three = 3
#
#     t = Table(
#         'data', MetaData(),
#         Column('value', Enum(MyEnum))
#
#     )

# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0417'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('fullname',String(50))
    # 浮点数的精确度不够精确
    # price = Column(Float)
    # 总共有多少位，保留几位小数
    price = Column(DECIMAL(20,5))       # 但是数据类型仍然是Float，删除重新映射
    is_delete = Column(Boolean)
    gender = Column(Enum('男', '女'))
    # gender = Column(Enum('男', '女'), default =  '男')     # 只能选这两个，写其他的会报错，default是默认选择
    create_time = Column(DateTime)
    content = Column(LONGTEXT)
    # onupdate (修改)更新就会触发的事件 可以写一个函数
    update_time = Column(DateTime, onupdate=datetime.now())

# 删除
Base.metadata.drop_all()
Base.metadata.create_all()

Session = sessionmaker(bind=engine)
session = Session()


user = User(name='corn', price= 1.3245223232, is_delete=False, gender='男', create_time=datetime(2020,5,3,21,35,23), content="xxxx")
session.add(user)
session.commit()

# onupdate案例
# user = session.query(User).first()
# print(user.name)
# user.name = 'xxx'
# session.commit()

# Date 日期 年月日
# DateTime 年月日 时分秒
# Time  时分秒


