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
    __tablename__ = 'art'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(50))
    author = Column(String(50))

    def __str__(self):
        return "Article(title:{},content:{},author:{})".format(self.title, self.content,self.author)

# Base.metadata.create_all()    # 运行之后就可以注释了
Session = sessionmaker(bind=engine)
session = Session()

def add_data():
    article = Article(title='python', content='人生苦短，我用python', author='龟叔')
    # article1 = Article(title='python', content='人生苦短，我用python', author='龟叔')
    session.add(article)
    # session.add_all([article, article1])
    session.commit()


def search_data():
    # all 是查询所有
    # data = session.query(Article).all()
    # for item in data:
    #     print(item)     # <__main__.Article object at 0x00000064C9F860C8>
    #     # Article(title:python,content:人生苦短，我用python,author:龟叔)
    #     # print(item.title)   # python
    #     # print(item.content)     # 人生苦短，我用python
    # print(data)

    # 条件 filter
    # data = session.query(Article).filter(Article.title=='python').all()
    # for item in data:
    #     print(item)


    # filter_by
    # data = session.query(Article).filter_by(title='Java').all()
    # for item in data:
    #     print(item)

    # 查询第一条
    # data = session.query(Article).first()
    # print(data)

    data = session.query(Article).get(4)    # None 空
    print(data)


def update_data():
    # 查询出这条要修改的记录
    article = session.query(Article).first()
    article.title = 'lgcoder'
    print(article.title)
    # 回滚 已经提交的就不能回滚了
    session.rollback()
    print(article.title)
    session.commit()


def delete_data():
    article = session.query(Article).first()
    # 误操作
    # is_delete     1 未删除  0 删除
    """
    此时一般会给数据一个字段 is_delete,赋值0或1，代表需要删除，和不需要删除
    查询语句时候，只需要多添加一个查询语句is_delete==1或者is_delete==0就行
    此时的数据文件比较安全，不会产生误操作，不会丢失
    """

    session.delete(article)
    session.commit()


if __name__=='__main__':
    # add_data()
    # search_data()
    update_data()
    # delete_data()