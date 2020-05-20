from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
# from models import User   在manage.py导入
from exts import db

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)

# db = SQLAlchemy(app)   导入db

# 定义模型 models

# 引用模型
# user = User(name='futongxue', email='123@qq.com', password=‘123’)
# db.session.add(user)
# db.session.commit()

# 运行报错 cannot import name 'User' from 'models'
# 互相导入 建立一个中间文件


@app.route("/")
def index():
    return "首页"


if __name__ == '__main__':
    app.run(debug=True)





