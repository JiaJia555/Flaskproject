from sqlalchemy import create_engine
from constants import DB_URL

#连接数据库
engine = create_engine(DB_URL,echo=True)

# 使用with语句连接数据库，如果发生异常会被捕获
with engine.connect() as con:
    # 先删除users表
    con.execute('drop table if exists authors')
    # 创建一个users表，有自增长的id和name
    con.execute('create table authors(id int primary key auto_increment, name varchar(25))')
    # 插入两条数据到表中
    con.execute('insert into persons(name) values("abc")')
    con.execute('insert into persons(name) values("xiaotuo")')
    # 执行查询操作
    results = con.execute('select * from persons')
    # 从查找的结果中遍历
    for result in results:
        print(result)