from flask import Flask, session, current_app, g
import os
from datetime import timedelta
import config
from utils import log_a, log_b


# print(os.random(24))  生成24位随机变化的数据
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)      # 数字是随便给的
# 设置到期时间
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

@app.route("/login/")
def login():
    # session 类似于字典
    session['username'] = 'futongxue'
    session['user_id'] = 1
    # 持久化
    session.permanent = True
    return "登陆页"


# print(current_app.name)   不能在视图函数外部调用
@app.route("/")
def index():
    username = session.get('username')
    # g 对象每次刷新页面 会被重置
    g.username = username
    # print(username)
    # print(current_app.name)

    log_a(username)
    log_b(username)
    # hell0()
    # print(current_app.config['DEBUG'])   # 不是读取current_app的配置文件
    # print(current_app.config['HOST'])     # 读取绑定在app的配置文件
    print(current_app.config['SECRET_KEY'])
    return "首页"

def hello():
    print("hello %s" % g.username)


@app.route('/logout/')
def logout():
    # 删除 username
    # session.pop('username')
    # 清空 session
    session.clear()
    return '退出登录'


if __name__ == '__main__':
    app.run(debug=True)