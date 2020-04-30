from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# 连接数据库 UPHPD
# 地址
HOSTNAME = "127.0.0.1"
# 数据库
DATABASE = 'demo0417' # 刚刚新建的数据库
# 端口
PORT = 3306
# 用户名和密码
USERNAME = 'root'
PASSWORD = 'root'
# 创建数据库引擎
# dialect(mysql/sqlmap)+driver://username:password@host:port/database?charset=utf8
DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
engine = create_engine(DB_URL)

# orm操作都要继承函数生成的基类
Base = declarative_base(engine)

# ORM操作数据库
class User(Base):
    # 定义表的名字
    __tablename__= "students"

    # 给一些字段 id name age gender
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)       # False为非空
    gender = Column(Integer, default=1, comment="1为男，2为女")

# 模型映射到数据库
Base.metadata.create_all()


