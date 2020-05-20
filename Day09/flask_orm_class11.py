from sqlalchemy import create_engine, Column, and_, or_, ForeignKey
from sqlalchemy import Integer, String, Float, DECIMAL, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
import random
from sqlalchemy.orm import relationship, backref

# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0422'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)

class User(Base):
    __tablename__ = "user1"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    # extend = relationship("UserExtend", uselist=False)


class UserExtend(Base):
    __tablename__="user_extend"
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50), nullable=False)

    uid = Column(Integer, ForeignKey("user1.id"))

    user = relationship("User", backref="extend")
    # user = relationship("User")
    # user = relationship("User", backref=backref("UserExtend", uselist=False))   # 代替上面的extend

Base.metadata.drop_all()
Base.metadata.create_all()

session = sessionmaker(bind=engine)()

user = User(username='futongxue')
# extend1 = UserExtend(school='lg')
# extend2 = UserExtend(school='lg')


# 添加数据
# extend1.user = user
# extend2.user = user
# session.add(extend1)
# session.add(extend2)
# session.commit()

# 现在表格不是一对一，是一对多，一个uid对应两个id.这种方法提交数据，即使设置了uselist还是可以提交多个数据，所以只能用下面的方法提交

# user.extend.append(extend1)
# user.extend.append(extend2)
#
# session.add(extend1)
# session.add(extend2)
# session.commit()

# 表格是一对一，所以无法添加两条数据，报错
# 问题：为什么user.extend一对一添加不行？