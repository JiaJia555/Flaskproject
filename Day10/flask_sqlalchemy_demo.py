from flask import Flask
from flask_sqlalchemy import SQLAlchemy

HOSTNAME = '127.0.0.1'
DATABASE = 'demo0424'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
app = Flask(__name__)
# engine = create_engine(DB_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False         # 解决 warnings

# Base = declarative_base(engine)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return "User{name: %s}" % self.name


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    # 外键
    uid = db.Column(db.Integer, db.ForeignKey("user.id"))

    author = db.relationship("User", backref='articles')


# Base.metadata.create_all()
# db.drop_all()
# db.create_all()

# session = sessionmaker(bind=engine)()
# 全部用db代替


# 添加数据
# user = User(name="futongxue")
# article = Article(title='python')
#
# article.author = user
# db.session.add(article)
# db.session.commit()

# 查询数据
# user = User.query.all()
# users = db.session.query(User).all()  都可以
# print(user)

# 排序
# users = User.query.order_by(User.id.desc()).all()

# 删除
# user = User.query.filter(User.name=='juran').first()
# db.session.delete(user)
# db.session.commit()


@app.route("/")
def index():
    return "首页"

if __name__ == '__main__':
    app.run(debug=True)

