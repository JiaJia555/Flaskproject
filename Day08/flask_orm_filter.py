from sqlalchemy import create_engine, Column, and_, or_
from sqlalchemy import Integer, String, Float, DECIMAL, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Date, DateTime, Time
from datetime import datetime, date, time
from sqlalchemy.dialects.mysql import LONGTEXT
import random


# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0417'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)

class Article(Base):
    __tablename__ = 'article2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    price = Column(Float, nullable=False)

    def __str__(self):
        return "Article(title:{}, price:{}".format(self.title, self.price)

# Base.metadata.drop_all()
Base.metadata.create_all()

Session = sessionmaker(bind=engine)
session = Session()

# for i in range(6):
#     article = Article(title="title%s" % i, price=random.randint(1,50))
#     session.add(article)
#
#
# session.commit()

# 过滤条件
# equals/not equals
# result = session.query(Article).filter(Article.title == "title0").all()
# result = session.query(Article).filter(Article.title != "title0").all()
# for data in result:
#     print(data)     # Article(title:title0, price:1.0
# print(result)       # [<__main__.Article object at 0x00000076426F9A48>]

# 模糊查询 like 例如 jia Python
# title 包含1
# result = session.query(Article).filter(Article.title.like('%1%')).all()
# Article(title:title1, price:8.0

# in/not in Python关键字 _私有的
# in[1,4] 查询的id是1,4
# result = session.query(Article).filter(Article.title.in_(['title0', 'title4'])).all()
# 虽然元组也可以，但是不建议使用，源码没有，但是可以列表嵌套元组

# result = session.query(Article).filter(-Article.title.in_(['title0', 'title4'])).all()
# result = session.query(Article).filter(Article.title.notin_(['title0', 'title4'])).all()

# Null != 空 null不可以可以查询，空可以
# result = session.query(Article).filter(Article.title == None).all()
# result = session.query(Article).filter(Article.title.is_(None).all())
# Article(title:None, price:13.0
# result = session.query(Article).filter(Article.title != None).all()
# result = session.query(Article).filter(Article.title.isnot(None)).all()
# 空不是None,数据库中占有空间的 输出Article(title:, price:14.0

# and
# result = session.query(Article).filter(Article.title == 'title0', Article.price == 40 ).all()
# result = session.query(Article).filter(and_(Article.title == 'title0', Article.price == 40)).all()
# result = session.query(Article).filter(Article.title == 'title0').filter( Article.price == 40).all()

# or 满足一个条件就可以
result = session.query(Article).filter(or_(Article.title == 'title0', Article.price == 30)).all()
for data in result:
    print(data)







