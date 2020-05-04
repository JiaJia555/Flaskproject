from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, Float, DECIMAL, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Date, DateTime, Time
from datetime import datetime, date, time
from sqlalchemy.dialects.mysql import LONGTEXT
import random
from sqlalchemy import func

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
    __tablename__ = 'article1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    def __str__(self):
        return "Article(title:{}, price:{}".format(self.title, self.price)

Base.metadata.create_all()

Session = sessionmaker(bind=engine)
session = Session()

# for i in range(6):
#     article = Article(title="title%s" % i, price=random.randint(1,50))
#     session.add(article)


# session.commit()

# query指定查询模型对象,属性
# articles = session.query(Article).all()
# print(articles)
# for article in articles:
#     print(article)      # Article(title:title5, price:15.0
#     print(article.title)


# query 聚合函数
# result = session.query(func.count(Article.id))
# print(result)
# SELECT count(article1.id) AS count_1 FROM article1 输出ORM转换的sql语句，运行之后输出6

# result = session.query(func.count(Article.id)).first()
# print(result)           # (6,)
# result = session.query(func.avg(Article.price)).first()
# print(result)       # (26.333333333333332,)

result = session.query(func.max(Article.price)).first()
print(result)       # (50.0,)

result = session.query(func.sum(Article.price)).first()
print(result)       # (158.0,)


