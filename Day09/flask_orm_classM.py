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

# 多对多
# 先创建中间表
"""
mytable = Table("mytable", metadata,
                Column('mytable_id', Integer, foreign_key=True),
                Column('value', String(50))
        )
"""
# 中间表的定义
teacher_classes = Table(
    "teacher_classes", Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teachers.id')),
    Column('class_id', Integer, ForeignKey('classes.id'))
)

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    classes = relationship('Classes', backref='teacher', secondary=teacher_classes)

    def __str__(self):
        return "Teacher:(name:%s)" % self.name

class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    def __str__(self):
        return "Class:(name:%s)" % self.name

# Base.metadata.drop_all()
Base.metadata.create_all()
session = sessionmaker(bind=engine)()

# teacher1 = Teacher(name='juran')
# teacher2 = Teacher(name='amy')
#
# classes1 = Classes(name="基础班")
# classes2 = Classes(name='进阶班')
#
# teacher1.classes.append(classes1)
# teacher2.classes.append(classes2)
#

# session.add(teacher1)
# session.add(teacher2)
# session.commit()


# 查询老师
teacher = session.query(Teacher).first()
print(teacher)          # Teacher:(name:juran)
# 查询老师对应的班级
for i in teacher.classes:
    print(i)            # Class:(name:基础班)


# 查询班级
classes = session.query(Classes).first()
print(classes)      # Class:(name:基础班)
# 查询班级对应的老师
for i in classes.teacher:
    print(i)        # Teacher:(name:juran)










