from sqlalchemy import create_engine, Column, ForeignKey
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

class Article(Base):
    __tablename__ = "article1"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    # create_time = Column()

    # def __repr__(self):
    def __str__(self):
        return "article:(title:%s)" % self.title


    # __mapper_args__ = {
    #     "order_by": id.desc()
    #     # "order_bu": -id
    # }


# Base.metadata.drop_all()
Base.metadata.create_all()
session = sessionmaker(bind=engine)()

# for i in range(10):
#     article = Article(title='title%s' % i)
#     session.add(article)
#
# session.commit()
# order_by默认 升序
# articles = session.query(Article).order_by(Article.id).all()
# 降序
# articles = session.query(Article).order_by(Article.id.desc()).all()
# articles = session.query(Article).order_by(-Article.id).all()

# articles = session.query(Article).all()
# print(articles)     # 打印在列表里面

# 前2条数据
# articles = session.query(Article).limit(2).all()
# [article:(title:title9), article:(title:title8)]

# 3-5 条数据  offset 从零开始 limit 偏移量
# articles = session.query(Article).offset(2).limit(3).all()

# articles = session.query(Article).order_by(Article.id.desc()).offset(2).limit(3).all()
# [article:(title:title7), article:(title:title6), article:(title:title5)]

# articles = session.query(Article).limit(3).offset(2).all()
# [article:(title:title2), article:(title:title3), article:(title:title4)]


# 切片
# articles = session.query(Article).all()[2:4]        # 左闭右开
# [article:(title:title2), article:(title:title3)]







