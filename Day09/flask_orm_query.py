
# class Article(Base):
#     __tablename__=

# 1.过滤条件过滤
# eq
result = session.query(Article).filter(Article.title=='title0'),all()
for data in result:
    print(data)
print(result)
# not eq    mysql<>
result = session.query(Article).filter(Article.title !='title0'),all()
for data in result:
    print(data)
print(result)

# like模糊查询 eg名字含有jia
# title包含 title title1 %表示任意字符
result = session.query(Article).filter(Article.title.like('%title%')),all()
result = session.query(Article).filter(Article.title.like('%title%'))
print(result)
for data in result:
    print(data)

# in python关键字 _私有的方法
# in[1,4] 查询的是id为1,4
result = session.query(Article.filter(Article.title.in_(['title1,'title4]))).all
for data in result:
    print(data)

# not in
result = session.query(~Article.filter(Article.title.in_(['title1,'title4]))).all
result = session.query(Article.filter(Article.title.notin_(['title1,'title4]))).all

# isnull, Null和空是不一样的,null没有开辟空间，空，开辟了空间
result - session.query(Aricle).filter(Article.title == None)).all()
result - session.query(Aricle).filter(Article.title.is_(None)).all()
result - session.query(Aricle).filter(Article.title != None).all()

# and
result - session.query(Aricle).filter(Article.title == 'title0', Article.pirce ==48).all()
result - session.query(Aricle).filter(and_(Article.title == 'title0', Article.pirce ==48)).all()
result - session.query(Aricle).filter(Article.title == 'title0').filter(Article.pirce ==48).all()
print(result)

# or    满足一个条件即可
result - session.query(Aricle).filter(or_(Article.pirce ==48)).all()



for data in result:
    print(data)
