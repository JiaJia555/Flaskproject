# 环境搭建
# pip install pipenv
# d:
# cd C:\Users\shelleyfu\Desktop\python learning         这个是自己第一次随便找的路径，但是是错误的，一定要切换到Pycharm创建的flask项目的文件路径
# 我的路径是这个 C:\Users\shelleyfu\Downloadbyjia\Flask框架
# pipenv shell     创建虚拟环境
# dir
# pip list
# pip install flask
# pip list
# pipenv install --dev + package可以记录安装库 一般不用

# pipenv shell        进入虚拟环境
# exit                退出虚拟环境
# pipenv -rm          删除整个环境 不会删除pipfile

# 最基本的flask应用
from flask import Flask
# from flask import config
import config       # 导入本地文件config.py
from flask import request

app = Flask(__name__)
# 装饰器    http://127.0.0.1:5000/  URL
@app.route("/")         # 根目录（首页）不写反斜线也可以，但是写了反斜线更清楚的代表了根目录
def hello_world():
    # a = 1         # 重启服务显示server error
    # b = 0
    # c = a/b
    return "hello world"

@app.route("/jiajia/")
def hello_jiajia():
    return "这是我的第一个Flask页面"

@app.route("/list/<int:aid>")       # http://127.0.0.1:5000/list/2
def article_list(aid):
    return"这是第{}篇文章".format(aid)

# path： 和string类似，但是可以传递斜杠/。
@app.route("/list/<path:aid>")
def article_detail(aid):
    return "detail-这是第{}篇文章".format(aid)

# any：可以指定多种路径
# article blog
@app.route("/<any(article, blog):url_path>/")
def item(url_path):
    return url_path

# 路径包含?参数
# https://www.baidu.com/s?wd=python
# wd?name=jiajia
@app.route("/wd")
def baidu():
    return request.args.get("name")


# 1. 重启debug model
if __name__ =="__main__":
    app.run(debug=True)
# 1. app.run(debug=True)                                # 自动重启 并且显示ZeroDivisionError
    # 2. app.debug = True
    # 3. app.config.update(DEBUG=True)                  # 配置文件（字典）
    # print(type(app.config))                           # 或者 print(isinstance(app.config,dict))
    # app.config.from_object(config)
    # app.config.from_object('config', silent=True)        # 通过字符串的方式也可以

# Debugger PIN: 330-049-915         运行显示的其中一个项目，输入之后进入类似于ipython的交互环境

# 2. 配置文件 config
# app.config.from_object(config)
# app.config.from_object('config')
# app.config.from_pyfile("config.py", silent=True)










