from sqlalchemy import create_engine, Column, and_, or_, ForeignKey
from sqlalchemy import Integer, String, Float, DECIMAL, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
import random
from sqlalchemy.orm import relationship

# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0422'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)

# 一对多 表关系
class Article(Base):
    __tablename__ ='article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    content = Column(LONGTEXT, nullable=False)
    uid = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))
    # author = relationship("User")

    def __str__(self):
        return "Article(title:%s)" % self.title

# 一个用户有多篇文章
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    # 反向访问属性
    articles = relationship("Article", backref='author')

    def __str__(self):
        return "User(username:%s)" % self.username

# Base.metadata.drop_all()
Base.metadata.create_all()

session = sessionmaker(bind=engine)()

# 查询 根据文章查询作者
article = session.query(Article).first()
print(article.author)

# 根据作者查询文章
# user = session.query(User).first()
# articles = user.articles
# for data in articles:
#     print(data)
# print(user.articles)

# 添加单条数据
# user = User(username='ftx')
# article = Article(title="Python", content='xxx')
# article.author = user
# session.add(article)
# session.commit()

# 添加多条文章的数据
# user = User(username='ftx')
# user = session.query(User).first()    # 在原来的作者中添加
# article1 = Article(title="Python1", content='xxx')
# article2 = Article(title="Python2", content='xxx')
#
# article1.author = user
# article1.author = user
#
# session.add_all([article1, article2])
# session.commit()

