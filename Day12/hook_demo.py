from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")                     # 3 第三执行
def index():
    # raise IndexError("index.error")   # 还是显示下面的404.html
    abort(404)   # 主动抛出404异常
    # 1/0
    # username = "futongxue"
    return render_template("index.html")        # 捕获 404
    # 1/0                           # debug=True 只会执行 1 2, False 都会执行
    # print("这是首页")
    # return "这是首页"


@app.route("/list/")
def list():
    # username = "futongxue"
    return render_template("list.html")

# 上下文管理器
@app.context_processor
def context():
    return {"username": "lgcoder"}


# @app.before_first_request
# def handle_first_request():
#     print("这是第一次请求之前执行的")   # 1 最先执行
#
#
# @app.before_request
# def handle_before():
#     print("每次请求之前被执行的")     # 2 第二执行
#
#
# @app.after_request
# def handel_after(response):
#     print("每次请求之后被执行的")
#     return response
#
#
# @app.teardown_appcontext
# def handle_teardown(response):
#     print("handle_teardown 被执行")
#     return response

@app.errorhandler(404)
def page_not_find(error):
    # return "页面不存在", 404
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):
    return "服务器内部错误"        # 1/0 debug 模式关闭
    # return render_template("500.html"), 500

if __name__ == '__main__':
    app.run()       # 上线 部署到服务器 别人去访问 debug 模式一定要关闭
    # app.run(debug=True)

# 这是第一次请求之前执行的  只有第一次才会被执行
# 每次请求之前被执行的
# 这是首页
# 每次请求之后被执行的
# handle_teardown 被执行