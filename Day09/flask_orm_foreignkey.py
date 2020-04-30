


# User / Article
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key= True)



session = sessionmaker(bind=engine)()
user = User(username='jiajia')
session.add(user)
session.commit()

article = Article(title='python', content="xxx", uid=1)
session.add(artciel)
session.commit()

