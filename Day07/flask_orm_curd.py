from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0417'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)

# 添加数据
class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

# Base.metadata.create_all()  # 映射数据库
article = Article(name="jiajia")
article1 = Article(name='lgcoder')
# print(article.name)     # jiajia
# print(article.id)       # None 还没提交写入数据库

# 提交到数据库
# 类的实例化 内部有__call__方法可以调用，将类变成方法
Session = sessionmaker(bind=engine)
session = Session()

# session.add(article1)     # 添加一条记录
session.add_all([article, article1])    # 添加2条或者多条
# print(article.name)     # jiajia
# print(article.id)       # None

# 提交
session.commit()
print(article.name)     # jiajia
print(article.id)       # 1

def delete_data():
    article = session.query(Article).first()
    # 误操作
    # is_delete  (不会)   1 未删除  0 删除
    """
    此时一般会给数据一个字段 is_delete,赋值0或1，代表需要删除，和不需要删除
    查询语句时候，只需要多添加一个查询语句is_delete==1或者is_delete==0就行
    此时的数据文件比较安全，不会产生误操作，不会丢失
    """

    session.delete(article)
    session.commit()