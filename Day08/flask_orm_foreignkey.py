from sqlalchemy import create_engine, Column, and_, or_, ForeignKey
from sqlalchemy import Integer, String, Float, DECIMAL, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Date, DateTime, Time
from datetime import datetime, date, time
from sqlalchemy.dialects.mysql import LONGTEXT
import random


# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0422'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)

# 类 User/Article
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))

    def __str__(self):
        return "User(username:%s)" % self.username


class Article(Base):
    __tablename__ ='article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    content = Column(LONGTEXT, nullable=False)

    # uid = Column(Integer, ForeignKey('user.id', ondelete='RESTRICT'))
    # uid = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))       # 级联删除
    uid = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))

Base.metadata.drop_all()
Base.metadata.create_all()


# 引擎 修改配置文件 mysql innodb允许外键 myisam不允许
# Session = sessionmaker(bind=engine)
# session = Session()
# 简写
session = sessionmaker(bind=engine)()

# 1 创建外键
user = User(username='futongxue')
session.add(user)
session.commit()

article = Article(title='python', content='xxx', uid=1)
# uid =2 (Background on this error at: http://sqlalche.me/e/gkpj)
session.add(article)
session.commit()

# 2.外键约束有以下几项：
    # 1. RESTRICT：父表数据被删除，会阻止删除。默认就是这一项。
    # 2. NO ACTION：在MySQL中，同RESTRICT, 无法删除
    # 3. CASCADE：级联删除，父级删除，子级也会被删除
    # 4. SET NULL：父表数据被删除，子表数据会设置为NULL。

# ORM 删除user表中的数据(这里需要重新建立表，)
    # RESTRICT：报错
    # CASCADE：级联删除，两个表中的数据全部变成Null
    # SET NULL：同上uid=Null
# user = session.query(User).first()
# print(user)
# # <__main__.User object at 0x0000000C39893848>有数据的
# session.delete(user)
# session.commit()

# 外键的查询 知道文章找作者 两步
# article = session.query(Article).first()
# uid = article.uid       # 取出uid
#
# user = session.query(User).get(uid)     # 找到User表uid对应的作者
# print(user)

# 一步
# user = session.query(User).filter(user.id == Article.uid).first()
# print(user)

