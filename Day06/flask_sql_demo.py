from flask import Flask
from sqlalchemy import create_engine

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

# 创建连接
with engine.connect() as conn:
    # 执行SQL语句，原生的SQL写法 ORM
    result = conn.execute("select * from users")
    print(result)
    # <sqlalchemy.engine.result.ResultProxy object at 0x0000008CDF85E988>
# 解决Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 518") result = self._query(query)
# pip install mysql-connector
# pymysql 改为mysqlconnector

# orm
# class Users(object):
#     name = "futongxue"
#     pass

# 类->一张表
# 属性->表字段
# 实例对象->一条记录

# user = Users(1, "futongxue")
# user.add()












