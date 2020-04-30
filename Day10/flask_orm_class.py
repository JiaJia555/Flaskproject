class User(Base):
    __tablename__  = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullbale=False)
    extend = relationship("UserExtend")

class UserExtend(Base):
    __tablename__="user_extend"
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    # 外键
    uid = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")


user = User(username="jiajia")
extend1 = UserExtend(school='lg')
